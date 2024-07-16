from django.contrib import admin
from .models import Category, Product


# Register your models here.
class CategoryModelAdmin(admin.ModelAdmin):
    # 一覧画面の表示項目の設定
    list_display = ('id', 'name', 'create_at', 'update_at')
    # ソート
    ordering = ('id',) # 逆順の場合は「-」を先頭につける. ('-id')
    # 追加・編集画面の表示項目の設定
    fields = ('name',)

class ProductModelAdmin(admin.ModelAdmin):
    # 一覧画面の表示項目の設定
    list_display = ('id', 'name', 'price', 'stock')
    ordering = ('id',)


admin.site.register(Category, CategoryModelAdmin)
admin.site.register(Product, ProductModelAdmin)
