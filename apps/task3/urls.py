from django.urls import path

from apps.task3.api_endpoints import ProductListAPIView

app_name = "task3"

urlpatterns = [
    path("productlist/", ProductListAPIView.as_view(), name="product_list"),
]
