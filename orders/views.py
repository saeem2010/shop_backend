from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Order, OrderItem

@api_view(['POST'])
def create_order(request):
    cart_items = request.data.get('cart_items', [])
    total_quantity = sum(item['quantity'] for item in cart_items)
    total_amount = sum(item['price'] * item['quantity'] for item in cart_items)

    try:
        # Create order
        order = Order.objects.create(
            total_quantity=total_quantity,
            total_amount=total_amount,
        )

        # Create order items
        for item in cart_items:
            OrderItem.objects.create(
                order=order,
                product_id=item['productId'],
                product_name=item['name'],
                product_description=item['description'],
                product_image=item['image'],
                product_price=item['price'],
                quantity=item['quantity'],
            )

        return Response({"message": "Order placed successfully", "order_id": order.order_id}, status=status.HTTP_201_CREATED)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['GET'])
def list_orders(request):
    orders = Order.objects.all().order_by('-created_at')
    data = [
        {
            "order_id": order.order_id,
            "description": order.description,
            "total_quantity": order.total_quantity,
            "total_amount": order.total_amount,
            "created_at": order.created_at,
            "status": order.status,
        }
        for order in orders
    ]
    return Response(data, status=status.HTTP_200_OK)


@api_view(['GET'])
def order_details(request, order_id):
    try:
        order = Order.objects.get(order_id=order_id)
        items = order.order_items.all()
        data = {
            "order_id": order.order_id,
            "created_at": order.created_at,
            "total_quantity": order.total_quantity,
            "total_amount": order.total_amount,
            "status": order.status,
            "items": [
                {
                    "product_name": item.product_name,
                    "product_description": item.product_description,
                    "product_image": item.product_image,
                    "product_price": item.product_price,
                    "quantity": item.quantity,
                    "total_price": item.get_total_price(),
                }
                for item in items
            ],
        }
        return Response(data, status=status.HTTP_200_OK)
    except Order.DoesNotExist:
        return Response({"error": "Order not found"}, status=status.HTTP_404_NOT_FOUND)
