from django.contrib import admin
from .models import Gig, Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name")


@admin.register(Gig)
class GigAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "title",
        "seller",
        "category",
        "price",
        "total_stock",
        "created_at",
    )
    list_filter = (
        'category',
        'bestseller',
        'created_at'
    )

    readonly_fields = ('created_at',)
