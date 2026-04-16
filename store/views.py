from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response


@api_view()
def product_list(request: Request) -> Response:
    return Response("ok")


@api_view()
def product_detail(request: Request, product_id: str) -> Response:
    return Response(product_id)
