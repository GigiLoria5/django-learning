from django.db.models import F, Model, OuterRef, Subquery
from django.db.models.aggregates import Sum
from django.shortcuts import render

from store.models import Collection, Product


def say_hello(request):
    highest_revenue_product = (
        Product.objects.filter(
            collection=OuterRef("pk"),
            orderitem__isnull=False,
        )
        .annotate(revenue=Sum(F("orderitem__quantity") * F("orderitem__unit_price")))
        .order_by("-revenue", "id")[:1]
    )
    queryset = (
        Collection.objects.annotate(
            product_title=Subquery(highest_revenue_product.values("title")),
            sales_revenue=Subquery(highest_revenue_product.values("revenue")),
        )
        .order_by("title")
        .values("title", "product_title", "sales_revenue")
    )
    result = list(queryset)
    return render(request, "hello.html", {"name": "Gigi", "result": result})
