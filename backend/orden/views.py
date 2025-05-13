from rest_framework import viewsets, permissions
from .models import Order
from .serializers import OrderSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated

class OrderHistoryViewSet(viewsets.ModelViewSet):
    # Solo los usuarios autenticados pueden ver su historial de pedidos
    permission_classes = [IsAuthenticated]
    serializer_class = OrderSerializer
    
    def get_queryset(self):
        # Filtra los pedidos del usuario autenticado
        return Order.objects.filter(user=self.request.user)

class OrderViewSet(viewsets.ModelViewSet):
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['status']  # ✅ Filtrado por estado

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)
        
    @action(detail=True, methods=['post'])
    def complete(self, request, pk=None):
        order = self.get_object()

        # ✅ Solo 'empleado_tienda' o admin/staff pueden completar pedidos
        user = request.user
        if (
            not user.groups.filter(name='empleado_tienda').exists()
            and not user.is_staff
            and not user.is_superuser
        ):
            return Response(
                {'detail': 'No tienes permiso para completar este pedido.'},
                status=status.HTTP_403_FORBIDDEN
            )

        if order.status == 'COMPLETED':
            return Response({'detail': 'El pedido ya está completado.'}, status=status.HTTP_400_BAD_REQUEST)

        if order.status == 'CANCELLED':
            return Response({'detail': 'No se puede completar un pedido cancelado.'}, status=status.HTTP_400_BAD_REQUEST)

        order.status = 'COMPLETED'
        order.save()

        return Response({'detail': 'Pedido marcado como completado.'}, status=status.HTTP_200_OK)



    @action(detail=True, methods=['post'])
    def cancel(self, request, pk=None):
        order = self.get_object()

        # ❌ Ya está cancelado
        if order.status == 'CANCELLED':
            return Response({'detail': 'El pedido ya está cancelado.'}, status=status.HTTP_400_BAD_REQUEST)

        # ❌ Ya está completado
        if order.status == 'COMPLETED':
            return Response({'detail': 'El pedido ya fue completado y no puede cancelarse.'}, status=status.HTTP_400_BAD_REQUEST)

        # ✅ Restaurar stock
        for item in order.items.all():
            item.product.stock += item.quantity
            item.product.save()

        # Cambiar estado a cancelado
        order.status = 'CANCELLED'
        order.save()

        return Response({'detail': 'Pedido cancelado y stock restaurado.'}, status=status.HTTP_200_OK)
