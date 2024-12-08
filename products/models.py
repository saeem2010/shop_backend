# products/models.py
from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, default='')  # Provide a default value

    def __str__(self):
        return str(self.name)  # Returns the name of the category for display

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField(default=0)  # Provide a default value
    image = models.ImageField(upload_to='products/', blank=True, null=True)  # Allow null if no image is provided

    def __str__(self):
        return str(self.name)  # Returns the name of the product for display
