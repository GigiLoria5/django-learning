from decimal import Decimal

from rest_framework import serializers

from store.models import Collection, Product

TAX_RATE = Decimal(1.22)


class CollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collection
        fields = ["id", "title", "products_count"]

    products_count = serializers.IntegerField(read_only=True)


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            "id",
            "title",
            "description",
            "slug",
            "inventory",
            "unit_price",
            "price_with_tax",
            "collection",
            # "collection_link",
        ]

    price_with_tax = serializers.SerializerMethodField(method_name="calculate_tax")
    # collection_link = serializers.HyperlinkedRelatedField(
    #     queryset=Collection.objects.all(),
    #     view_name="collection-detail",
    #     source="collection",
    # )

    @staticmethod
    def calculate_tax(product: Product) -> Decimal:
        return round(product.unit_price * TAX_RATE, 2)
