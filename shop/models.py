from django.db import models
from account.models import CustomUser


# Create your models here.
class Category(models.Model):
    class Meta:
        db_table = 'categories'
        verbose_name = 'カテゴリー'
        verbose_name_plural = 'カテゴリー'

    name = models.CharField(verbose_name='種別名', max_length=255)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    class Meta:
        db_table = 'products'
        verbose_name = 'プロダクト'
        verbose_name_plural = 'プロダクト'

    name = models.CharField(verbose_name='商品名', max_length=255)
    description = models.TextField(verbose_name='商品詳細', null=True, blank=True)
    price = models.DecimalField(verbose_name='価格', max_digits=10, decimal_places=2)
    stock = models.IntegerField(verbose_name='在庫')
    image = models.ImageField(verbose_name='商品画像', upload_to='', null=True, blank=True)
    category_id = models.ForeignKey('Category', on_delete=models.PROTECT)
    create_at = models.DateTimeField(auto_now_add=True) # 登録日時
    update_at = models.DateTimeField(auto_now=True) # 更新日時

    def __str__(self):
        return self.name


class Cart(models.Model):
    class Meta:
        db_table = 'carts'
        verbose_name = 'カート'
        verbose_name_plural = 'カート'

    user_id = models.ForeignKey(CustomUser, on_delete=models.PROTECT)
    product_id = models.ForeignKey('Product', on_delete=models.PROTECT)
    quantity = models.IntegerField() # 個数
    create_at = models.DateTimeField(auto_now_add=True) # 登録日時
    update_at = models.DateTimeField(auto_now=True) # 更新日時

    def __str__(self):
        return f'{self.user_id}さんのカート({self.id})'
