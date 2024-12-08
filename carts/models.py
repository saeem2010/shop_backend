from django.db import models
from products.models import Product
from customers.models import Customer

class Cart(models.Model):
    customer = models.OneToOneField(Customer, on_delete=models.SET_NULL, null=True, blank=True)  # Allow null
    created_at = models.DateTimeField(auto_now_add=True)

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def get_total_price(self):
        return self.product.price * self.quantity
