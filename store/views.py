from django.db.models import Count
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.generics import get_object_or_404
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from store.models import Collection, Product
from store.serializers import CollectionSerializer, ProductSerializer


class ProductList(APIView):
    def get(self, request: Request) -> Response:
        products_qs = Product.objects.all().select_related("collection")
        serialized_products = ProductSerializer(
            products_qs, many=True, context={"request": request}
        )
        return Response(serialized_products.data)

    def post(self, request: Request) -> Response:
        serialized_product = ProductSerializer(data=request.data)
        serialized_product.is_valid(raise_exception=True)
        serialized_product.save()
        return Response(serialized_product.data, status=status.HTTP_201_CREATED)


class ProductDetail(APIView):
    def get(self, request: Request, pk: str) -> Response:
        product = get_object_or_404(Product, pk=pk)
        serialized_product = ProductSerializer(product)
        return Response(serialized_product.data)

    def put(self, request: Request, pk: str) -> Response:
        product = get_object_or_404(Product, pk=pk)
        serialized_product = ProductSerializer(product, data=request.data)
        serialized_product.is_valid(raise_exception=True)
        serialized_product.save()
        return Response(serialized_product.data)

    def delete(self, request: Request, pk: str) -> Response:
        product = get_object_or_404(Product, pk=pk)
        if product.orderitems.count() > 0:
            return Response(
                {"error": "Product cannot be deleted because it is in an order."},
                status=status.HTTP_405_METHOD_NOT_ALLOWED,
            )
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(["GET", "POST"])
def collection_list(request: Request) -> Response:
    if request.method == "GET":
        queryset = Collection.objects.annotate(products_count=Count("products"))
        serialized_collections = CollectionSerializer(queryset, many=True)
        return Response(serialized_collections.data)
    elif request.method == "POST":
        serialized_collection = CollectionSerializer(data=request.data)
        serialized_collection.is_valid(raise_exception=True)
        serialized_collection.save()
        return Response(serialized_collection.data, status=status.HTTP_201_CREATED)
    return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view(["GET", "PUT", "DELETE"])
def collection_detail(request: Request, pk: str) -> Response:
    collection = get_object_or_404(
        Collection.objects.annotate(products_count=Count("products")), pk=pk
    )
    if request.method == "GET":
        serialized_collection = CollectionSerializer(collection)
        return Response(serialized_collection.data)
    elif request.method == "PUT":
        serialized_collection = CollectionSerializer(collection, data=request.data)
        serialized_collection.is_valid(raise_exception=True)
        serialized_collection.save()
        return Response(serialized_collection.data)
    elif request.method == "DELETE":
        if collection.products.count() > 0:
            return Response(
                {"error": "Collection cannot be deleted because it has products."},
                status=status.HTTP_405_METHOD_NOT_ALLOWED,
            )
        collection.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
