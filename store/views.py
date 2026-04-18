from rest_framework.decorators import api_view
from rest_framework.generics import get_object_or_404
from rest_framework.request import Request
from rest_framework.response import Response

from store.models import Collection, Product
from store.serializers import CollectionSerializer, ProductSerializer


@api_view()
def product_list(request: Request) -> Response:
    products_qs = Product.objects.all().select_related("collection")
    serialized_products = ProductSerializer(
        products_qs, many=True, context={"request": request}
    )
    return Response(serialized_products.data)


@api_view()
def product_detail(request: Request, pk: str) -> Response:
    product = get_object_or_404(Product, pk=pk)
    serialized_product = ProductSerializer(product)
    return Response(serialized_product.data)


@api_view()
def collection_detail(request: Request, pk: str) -> Response:
    collection = get_object_or_404(Collection, pk=pk)
    serialized_collection = CollectionSerializer(collection)
    return Response(serialized_collection.data)
