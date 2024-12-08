# carts/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CartViewSet, AddToCartView

# Set up the router for the CartViewSet
router = DefaultRouter()
router.register(r'carts', CartViewSet, basename='cart')

# Define the urlpatterns with the router and the add-to-cart path
urlpatterns = [
    path('', include(router.urls)),  # Include all router-registered URLs
    path('items/add/', AddToCartView.as_view(), name='add-to-cart'),  # Path for adding to cart
]
