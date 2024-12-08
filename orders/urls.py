# orders/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_order, name='create-order'),  # Endpoint for creating orders
    path('list/', views.list_orders, name='list-orders'),      # Endpoint for listing all orders
    path('<int:order_id>/details/', views.order_details, name='order-details'),  # Endpoint for order details
]
