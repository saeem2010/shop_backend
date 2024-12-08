# products/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'categories', views.CategoryViewSet)  # Route for CategoryViewSet
router.register(r'products', views.ProductViewSet)      # Route for ProductViewSet

urlpatterns = [
    path('', include(router.urls)),  # Include all registered routes
]
