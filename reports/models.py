# reports/models.py
from django.db import models

class Store(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Product(models.Model):
    store = models.ForeignKey(Store, related_name="products", on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

class Sale(models.Model):
    product = models.ForeignKey(Product, related_name="sales", on_delete=models.CASCADE)
    quantity = models.IntegerField()
    sold_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.quantity} of {self.product.name}"