# products/views.py
from rest_framework import viewsets
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Category, Product
from .serializers import CategorySerializer, ProductSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()  # Queryset for all categories
    serializer_class = CategorySerializer  # Use the CategorySerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()  # Queryset for all products
    serializer_class = ProductSerializer  # Use the ProductSerializer
    # Add the search and filtering backends
    filter_backends = (filters.SearchFilter, DjangoFilterBackend)
    search_fields = ('name', 'description')  # Fields to search in
    filterset_fields = ['category']  # Allow filtering by category
