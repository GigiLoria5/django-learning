from decimal import Decimal

from rest_framework import serializers

from store.models import Product, Collection

TAX_RATE = Decimal(1.22)


class CollectionSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField(max_length=255)


class ProductSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField(max_length=255)
    price = serializers.DecimalField(
        max_digits=6, decimal_places=2, source="unit_price"
    )
    price_with_tax = serializers.SerializerMethodField(method_name="calculate_tax")
    collection = serializers.HyperlinkedRelatedField(
        queryset=Collection.objects.all(), view_name="collection-detail",
    )

    @staticmethod
    def calculate_tax(product: Product) -> Decimal:
        return round(product.unit_price * TAX_RATE, 2)
