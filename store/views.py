from rest_framework.decorators import api_view
from rest_framework.generics import get_object_or_404
from rest_framework.request import Request
from rest_framework.response import Response

from store.models import Product
from store.serializers import ProductSerializer


@api_view()
def product_list(request: Request) -> Response:
    products_qs = Product.objects.all()
    serializer = ProductSerializer(products_qs, many=True)
    return Response(serializer.data)


@api_view()
def product_detail(request: Request, product_id: str) -> Response:
    product = get_object_or_404(
        Product, pk=product_id
    )
    serializer = ProductSerializer(product)
    return Response(serializer.data)
