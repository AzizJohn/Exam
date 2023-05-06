from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics

from apps.task3.models import Product

from apps.task3.api_endpoints.ProductList.serializers import ProductSerializer


class ProductListAPIView(generics.ListAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()


__all__ = ("ProductListAPIView",)
