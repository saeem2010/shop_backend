from django.db import models

class Order(models.Model):
    STATUS_CHOICES = [
        ('Processing', 'Processing'),
        ('Shipped', 'Shipped'),
        ('Delivered', 'Delivered'),
        ('Cancelled', 'Cancelled'),
    ]

    order_id = models.AutoField(primary_key=True)  # AutoField will automatically generate values for new rows
    customer_name = models.CharField(max_length=255, null=True, blank=True)  # Add customer if required
    total_quantity = models.PositiveIntegerField(default=0)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Processing')

    @property
    def description(self):
        items = self.order_items.all()
        if items.exists():
            first_item_name = items[0].product_name
            other_items_count = items.count() - 1
            if other_items_count > 0:
                return f"{first_item_name} and {other_items_count} other items"
            return first_item_name
        return "No items"

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='order_items')
    product_id = models.PositiveIntegerField()
    product_name = models.CharField(max_length=255)
    product_description = models.TextField(null=True, blank=True)
    product_image = models.URLField(null=True, blank=True)
    product_price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField()

    def get_total_price(self):
        return self.product_price * self.quantity
