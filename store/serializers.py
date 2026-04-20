from decimal import Decimal

from rest_framework import serializers

from store.models import Cart, CartItem, Collection, Product, Review

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
        ]

    price_with_tax = serializers.SerializerMethodField(method_name="calculate_tax")

    @staticmethod
    def calculate_tax(product: Product) -> Decimal:
        return round(product.unit_price * TAX_RATE, 2)


class SimpleProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ["id", "title", "unit_price"]


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ["id", "date", "name", "description"]

    def create(self, validated_data):
        product_id = self.context["product_id"]
        return Review.objects.create(product_id=product_id, **validated_data)


class CartItemSerializer(serializers.ModelSerializer):
    product = SimpleProductSerializer(read_only=True)
    total_price = serializers.SerializerMethodField(method_name="calculate_total_price")

    class Meta:
        model = CartItem
        fields = ["id", "product", "quantity", "total_price"]

    @staticmethod
    def calculate_total_price(cart_item: CartItem) -> Decimal:
        return Decimal(cart_item.quantity) * cart_item.product.unit_price


class CartSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)
    items = CartItemSerializer(many=True, read_only=True)
    total_price = serializers.SerializerMethodField(method_name="calculate_total_price")

    class Meta:
        model = Cart
        fields = ["id", "items", "total_price"]

    @staticmethod
    def calculate_total_price(cart: Cart) -> Decimal:
        return Decimal(
            sum(item.quantity * item.product.unit_price for item in cart.items.all())
        )
