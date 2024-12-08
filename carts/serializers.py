# carts/serializers.py
from rest_framework import serializers
from .models import Cart, CartItem
from products.models import Product

class CartItemSerializer(serializers.ModelSerializer):
    product = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all())  # Accept only the product ID
    quantity = serializers.IntegerField()

    class Meta:
        model = CartItem
        fields = ['product', 'quantity']  # Ensure 'product' and 'quantity' are included

class CartSerializer(serializers.ModelSerializer):
    items = CartItemSerializer(many=True, read_only=True)

    class Meta:
        model = Cart
        fields = ['id', 'items', 'created_at', 'updated_at']  # Explicit fields to be serialized
    
    def to_representation(self, instance):
        """Optimize how data is represented to reduce unnecessary data."""
        data = super().to_representation(instance)
        # You can further modify the cart representation here if needed
        # For example, include extra details such as the total price
        total_price = sum(item['product']['price'] * item['quantity'] for item in data['items'])
        data['total_price'] = total_price
        return data
