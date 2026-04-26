from django.contrib import admin
from django.db.models import Count, QuerySet
from django.http import HttpRequest
from django.urls import reverse
from django.utils.html import format_html
from django.utils.http import urlencode

from . import models


class InventoryFilter(admin.SimpleListFilter):
    title = "inventory"
    parameter_name = "inventory"

    def lookups(self, request, model_admin):
        return (
            ("<100", "Low"),
            (">=100", "OK"),
        )

    def queryset(self, request, queryset):
        if self.value() == "<100":
            return queryset.filter(inventory__lt=100)
        return queryset.filter(inventory__gte=100)


class ProductImageInline(admin.TabularInline):
    model = models.ProductImage
    readonly_fields = ("thumbnail",)

    def thumbnail(self, instance):
        if instance.image.name != "":
            return format_html(
                '<img src="{}" width="50" height="50" />', instance.image.url
            )
        return ""


@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    actions = ["clear_inventory"]
    inlines = [ProductImageInline]
    list_display = ("title", "unit_price", "inventory_status")
    list_editable = ("unit_price",)
    list_filter = ("collection", "last_updated", InventoryFilter)
    ordering = ("title",)
    list_per_page = 10

    @admin.display(ordering="inventory", description="Inventory Status")
    def inventory_status(self, product) -> str:
        if product.inventory < 100:
            return "Low"
        return "OK"

    @admin.action(description="Clear inventory")
    def clear_inventory(self, request, queryset):
        updated_count = queryset.update(inventory=0)
        self.message_user(request, f"Cleared inventory for {updated_count} products.")


@admin.register(models.Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "membership")
    list_editable = ("membership",)
    list_per_page = 10
    list_select_related = ("user",)
    ordering = ("user__first_name", "user__last_name")
    search_fields = ("first_name__istartswith", "last_name__istartswith")


@admin.register(models.Collection)
class CollectionAdmin(admin.ModelAdmin):
    list_display = ("title", "products_count")

    @admin.display(ordering="products_count", description="Products Count")
    def products_count(self, collection):
        url = f"{reverse('admin:store_product_changelist')}?{urlencode({'collection__id': collection.id})}"
        return format_html('<a href="{}">{}<a>', url, collection.products_count)

    def get_queryset(self, request: HttpRequest) -> QuerySet:
        return (
            super()
            .get_queryset(request)
            .annotate(products_count=Count("products", distinct=True))
        )


@admin.register(models.Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("id", "placed_at", "customer")
