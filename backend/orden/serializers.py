from rest_framework import serializers
from .models import Order, OrderItem
from productos.models import Product

class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ['product', 'quantity']
    def get_subtotal(self, obj):
        return obj.product.price * obj.quantity

from rest_framework.exceptions import ValidationError

class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True)
    total = serializers.SerializerMethodField()

    class Meta:
        model = Order
        fields = ['id', 'created_at', 'items', 'total','status', 'created_at']

    def create(self, validated_data):
        items_data = validated_data.pop('items')
        user = self.context['request'].user
        order = Order.objects.create(user=user)

        for item_data in items_data:
            product = item_data['product']
            quantity = item_data['quantity']

            # 🔴 Validar stock
            if product.stock < quantity:
                raise ValidationError(
                    f"No hay suficiente stock para {product.name}. Stock disponible: {product.stock}"
                )

            # ✅ Descontar stock y guardar
            product.stock -= quantity
            product.save()

            OrderItem.objects.create(order=order, product=product, quantity=quantity)

        return order

    def get_total(self, obj):
        return sum(item.product.price * item.quantity for item in obj.items.all())
