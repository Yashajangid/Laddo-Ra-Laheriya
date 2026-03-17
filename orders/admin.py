from django.contrib import admin
from .models import Order, OrderItem

class ItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    inlines = [ItemInline]
    list_display = ('id','buyer','status','total_amount','created_at')
