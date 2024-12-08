from django.contrib import admin
from .models import Order, OrderItem

class OrderAdmin(admin.ModelAdmin):
    list_display = ('customer_name', 'description', 'total_quantity', 'total_amount', 'status', 'created_at')
    list_filter = ('status', 'created_at')  # Optional: Add filters for admin
    search_fields = ('customer_name', 'status')  # Optional: Add search fields

class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('order', 'product_name', 'quantity', 'product_price', 'get_total_price')
    search_fields = ('product_name',)  # Optional: Add search fields

admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem, OrderItemAdmin)
