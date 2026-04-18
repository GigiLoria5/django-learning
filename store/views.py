from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.generics import get_object_or_404
from rest_framework.request import Request
from rest_framework.response import Response

from store.models import Collection, Product
from store.serializers import CollectionSerializer, ProductSerializer


@api_view(["GET", "POST"])
def product_list(request: Request) -> Response:
    if request.method == "GET":
        products_qs = Product.objects.all().select_related("collection")
        serialized_products = ProductSerializer(
            products_qs, many=True, context={"request": request}
        )
        return Response(serialized_products.data, status=status.HTTP_200_OK)
    elif request.method == "POST":
        serialized_product = ProductSerializer(data=request.data)
        serialized_product.is_valid(raise_exception=True)
        serialized_product.save()
        return Response(serialized_product.data, status=status.HTTP_201_CREATED)
    return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view(["GET", "PUT"])
def product_detail(request: Request, pk: str) -> Response:
    product = get_object_or_404(Product, pk=pk)
    if request.method == "GET":
        serialized_product = ProductSerializer(product)
        return Response(serialized_product.data, status=status.HTTP_200_OK)
    elif request.method == "PUT":
        serialized_product = ProductSerializer(product, data=request.data)
        serialized_product.is_valid(raise_exception=True)
        serialized_product.save()
        return Response(serialized_product.data, status=status.HTTP_200_OK)
    return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view()
def collection_detail(request: Request, pk: str) -> Response:
    collection = get_object_or_404(Collection, pk=pk)
    serialized_collection = CollectionSerializer(collection)
    return Response(serialized_collection.data)
