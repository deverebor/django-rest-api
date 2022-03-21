from pickletools import read_long1
from rest_framework import serializers

from .models import Product


def get_my_discount(obj):
    if not hasattr(obj, 'id'):
        return None
    if not isinstance(obj, Product):
        return None
    return obj.get_discount()


class ProductSerializer(serializers.ModelSerializer):
    my_discount = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Product
        fields = [
            'title',
            'content',
            'price',
            'sale_price',
            'my_discount',
        ]
