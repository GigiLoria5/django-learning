# Exercises

## 1) Total store value

Calculate the **total value of the whole store**. Formula: `inventory * unit_price`

<details>
<summary>Hints</summary>

* `aggregate()`
* `Sum`
* `F()` expressions
* arithmetic expressions

</details>

**Goal output**

```python
{'total_value': Decimal('73619.17')}
```

---

## 2) Revenue per product

For every product, show:

* product title
* total quantity sold
* total revenue

Sort by revenue descending.

<details>
<summary>Hints</summary>

* joins
* reverse relations
* `annotate()`
* multiple aggregates
* ordering by annotation

</details>

---

## 3) Top 10 best-selling products

Return the **top 10 products by quantity sold**.

<details>
<summary>Hints</summary>

* `Sum("orderitems__quantity")`
* sorting
* slicing queryset
* grouped annotations

</details>

---

## 4) Product count per collection

For each collection, show:

* collection title
* number of products

Sort highest first.

<details>
<summary>Hints</summary>

* reverse FK joins
* `Count`
* grouping
* ordering by annotation

</details>

---

## 5) Top 5 customers by spending

Show the top 5 customers by **total spend** and their full name.

Total spend = sum of all their order items.

<details>
<summary>Hints</summary>

* multi-hop joins
* `Sum(F() * F())`
* `Concat` function
* annotation over multiple tables
* ordering by computed totals

</details>

---

## 6) Monthly sales report

Show total revenue **grouped by month**.

<details>
<summary>Hints</summary>

* `TruncMonth`
* date grouping
* `annotate()`
* aggregation by time period

</details>

**Expected shape**

```python
[
    {"month": "2026-01", "sales_revenue": 12000},
    {"month": "2026-02", "sales_revenue": 18000},
]
```

---

## 7) Products never ordered

Find all products that were **never sold**.

<details>
<summary>Hints</summary>

* reverse joins
* `isnull`
* `exclude()`
* anti-join logic

</details>

---

## 8) Customers with no Books orders

Return customers who have placed at least one order, and none of those orders include
products from the `Books` collection

<details>
<summary>Hints</summary>

* reverse FK traversal
* `Count`
* filtering zero annotations
* `Q()` optional

</details>

The number of customers should be 133.

---

## 9) Most valuable order

Find the **single highest-value order**.

Order total = sum of all its items.

<details>
<summary>Hints</summary>

* per-order annotation
* aggregate expressions
* sorting by annotation
* `.first()`

</details>

---

## 10) Top product in each collection

For each collection, find the **product with the highest sales revenue**.

<details>
<summary>Hints</summary>

* `Subquery`
* `OuterRef`
* nested annotations
* advanced grouping logic

The result should include: collection title, product title, and total revenue.

</details>

---

# Solutions

## 1

```python
from django.db.models import F
from django.db.models.aggregates import Sum
from store.models import Product

queryset = Product.objects.aggregate(
    total_value=Sum(F("inventory") * F("unit_price")),
)
```

## 2

```python
from django.db.models import F
from django.db.models.aggregates import Sum
from store.models import Product

queryset = (
    Product.objects.filter(orderitem__isnull=False)
    .annotate(
        total_sales=Sum(F("orderitem__quantity")),
        total_revenue=Sum(F("orderitem__unit_price") * F("orderitem__quantity")),
    )
    .order_by("-total_revenue")
    .values("title", "total_sales", "total_revenue")
)
```

## 3

```python
from django.db.models.aggregates import Sum
from store.models import Product

queryset = (
    Product.objects.filter(orderitem__isnull=False)
    .annotate(total_quantity=Sum("orderitem__quantity"))
    .order_by("-total_quantity")
    .values("title", "total_quantity")
)[:10]
```

## 4

```python
from django.db.models.aggregates import Count
from store.models import Collection

queryset = (
    Collection.objects.annotate(product_count=Count("product"))
    .order_by("-product_count")
    .values("title", "product_count")
)
```

## 5

```python
from django.db.models import F, Value
from django.db.models.functions import Concat
from store.models import Customer

queryset = (
    Customer.objects.filter(order__orderitem__isnull=False)
    .annotate(
        total_spent=F("order__orderitem__quantity")
                    * F("order__orderitem__unit_price"),
        full_name=Concat("first_name", Value(" "), "last_name"),
    )
    .values("full_name", "total_spent")
    .order_by("-total_spent")[:5]
)
```

## 6

```python
from django.db.models import F, TextField, Value
from django.db.models.aggregates import Sum
from django.db.models.functions import Concat, Extract, Right
from store.models import Order

month = Concat(
    Extract("placed_at", "year"),
    Value("-"),
    Right(Concat(Value("0"), Extract("placed_at", "month")), 2),
    output_field=TextField(),
)
queryset = (
    Order.objects.annotate(month=month)
    .order_by("month")
    .values("month")
    .annotate(
        sales_revenue=Sum(F("orderitem__quantity") * F("orderitem__unit_price")),
    )
)
```

## 7

```python
from store.models import Product

queryset = Product.objects.exclude(orderitem__isnull=False).values("title")
# Same as: Product.objects.filter(orderitem__isnull=True).values("title") 
```

## 8

```python
from django.db.models import Exists, OuterRef, Q
from store.models import Customer, OrderItem

# Filter version
queryset = (
    Customer.objects.filter(order__isnull=False)
    .exclude(order__orderitem__product__collection__title="Books")
    .values("email")
    .order_by("email")
    .distinct()
)

# Exists version
books_orders = OrderItem.objects.filter(
    order__customer=OuterRef("pk"),
    product__collection__title="Books",
)
queryset = (
    Customer.objects.filter(order__isnull=False)
    .annotate(has_books_order=Exists(books_orders))
    .filter(has_books_order=False)
    .values("email")
    .order_by("email")
    .distinct()
)

# Q Version
queryset = (
    Customer.objects.exclude(
        Q(order__isnull=True)
        | Q(order__orderitem__product__collection__title="Books")
    )
    .values("email")
    .order_by("email")
    .distinct()
)
```

## 9

```python
from django.db.models import F
from django.db.models.aggregates import Sum
from store.models import Order

result = (
    Order.objects.filter(orderitem__isnull=False)
    .annotate(total=Sum(F("orderitem__quantity") * F("orderitem__unit_price")))
    .order_by("-total")
    .values("pk", "total")
    .first()
)
```

## 10

```python
from django.db.models import F, OuterRef, Subquery
from django.db.models.aggregates import Sum
from store.models import Collection, Product

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
```
