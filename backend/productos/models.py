from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    stock = models.PositiveIntegerField(default=0)
    image = models.ImageField(upload_to='productos/', blank=True, null=True)
    category = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name} ({self.stock} disponibles)"
