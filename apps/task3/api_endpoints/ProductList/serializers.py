from rest_framework import serializers

from apps.task3.models import Product
from apps.task3.utils import encrypt


class ProductSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()
    price = serializers.SerializerMethodField()
    marja = serializers.SerializerMethodField()
    package_code = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = (
            "id",
            "name",
            "price",
            "marja",
            "package_code",
        )

    def get_name(self, obj):
        return encrypt(obj.name)['cipher_text']

    def get_price(self, obj):
        return encrypt(str(obj.price))['cipher_text']

    def get_marja(self, obj):
        return encrypt(str(obj.marja))['cipher_text']

    def get_package_code(self, obj):
        return encrypt(obj.package_code)['cipher_text']
