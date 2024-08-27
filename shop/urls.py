from django.urls import path
from shop import views

app_name = 'shop'
urlpatterns = [
    path("", views.index, name="index"),
    path("product/search/", views.product_search, name="product_search"),
    path("product/detail/<int:product_id>", views.product_detail, name="product_detail"),
    path("cart/", views.cart, name="cart"),
    path("cart/add/<int:product_id>", views.cart_add, name="cart_add"),
]
