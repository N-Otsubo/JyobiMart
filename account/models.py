from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class CustomUser(AbstractUser):
    class Meta:
        db_table = 'custom_users'
        verbose_name = 'カスタムユーザー' # 単数形
        verbose_name_plural = 'カスタムユーザー' # 複数形

    post_code = models.CharField(verbose_name="郵便番号", max_length=10)
    address = models.CharField(verbose_name="住所", max_length=255)
    phone_number = models.CharField(verbose_name="電話番号", max_length=15)

    def __str__(self):
        return self.username
