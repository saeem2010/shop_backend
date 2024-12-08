from django.db import models
from orders.models import Order
from django.utils import timezone

class Payment(models.Model):
    order = models.OneToOneField(Order, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method = models.CharField(max_length=50, default='COD')  # Cash On Delivery
    payment_status = models.CharField(max_length=50, default='Pending')
    created_at = models.DateTimeField(auto_now_add=True)  # Keep this as it is

    def __str__(self):
        return f"Payment for Order {self.order.id}"
