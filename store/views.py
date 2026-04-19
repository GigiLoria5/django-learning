from django.db.models import Count
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.generics import ListCreateAPIView, get_object_or_404
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from store.models import Collection, Product
from store.serializers import CollectionSerializer, ProductSerializer


class ProductList(ListCreateAPIView):
    queryset = Product.objects.select_related("collection").all()
    serializer_class = ProductSerializer

    def get_serializer_context(self):
        return {"request": self.request}


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


class CollectionList(ListCreateAPIView):
    queryset = Collection.objects.annotate(products_count=Count("products")).all()
    serializer_class = CollectionSerializer


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
