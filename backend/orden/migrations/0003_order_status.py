# Generated by Django 5.2.1 on 2025-05-13 21:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orden', '0002_remove_order_product_remove_order_quantity_orderitem'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('PENDING', 'Pendiente'), ('CANCELLED', 'Cancelado'), ('COMPLETED', 'Completado')], default='PENDING', max_length=20),
        ),
    ]
