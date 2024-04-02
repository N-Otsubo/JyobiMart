from django.contrib import admin
from .models import Product, Category, Order, OrderDetail, Cart

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'price', 'stock', 'category_id', 'created_at', 'updated_at')
    list_filter = ('category_id',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    ordering = ('id',)


class CartAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'product_id', 'quantity', 'created_at')
    list_display_links = ('user_id', 'product_id')
    list_filter = ('user_id', 'product_id')

admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Order)
admin.site.register(OrderDetail)
admin.site.register(Cart, CartAdmin)