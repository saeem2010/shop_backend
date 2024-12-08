# carts/views.py
from rest_framework import status, viewsets
from rest_framework.parsers import JSONParser
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from products.models import Product
from .models import Cart, CartItem
from .serializers import CartItemSerializer, CartSerializer

class CartViewSet(viewsets.ReadOnlyModelViewSet):  # Read-only to view cart data
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    permission_classes = [AllowAny]  # Allowing anyone to read cart information

class AddToCartView(APIView):
    parser_classes = [JSONParser]  # Ensure JSON data parsing only

    def post(self, request):
        # Log the incoming request data for debugging
        print("Request data:", request.data)

        # Retrieve productID and quantity from the JSON request body
        product_id = request.data.get("productID")
        quantity = request.data.get("quantity")

        # Check if both productID and quantity are provided
        if product_id is None or quantity is None:
            return Response(
                {"error": "Both productID and quantity are required."},
                status=status.HTTP_400_BAD_REQUEST
            )

        # Check that the product exists
        try:
            product = Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            return Response(
                {"error": "Product not found."},
                status=status.HTTP_404_NOT_FOUND
            )

        # Get or create the cart for the user (using request.user for authenticated users)
        cart, _ = Cart.objects.get_or_create(user=request.user)

        # Create or update the cart item with the provided quantity
        cart_item, created = CartItem.objects.update_or_create(
            cart=cart,
            product=product,
            defaults={"quantity": quantity}
        )

        # Return the serialized cart item data as the response
        return Response(CartItemSerializer(cart_item).data, status=status.HTTP_201_CREATED)
