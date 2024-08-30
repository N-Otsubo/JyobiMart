from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import TemplateView
from .models import Product, Cart


# Create your views here.
class IndexView(TemplateView):
    template_name = 'shop/index.html'


class ProductSearchView(View):
    def get(self, request):
        # 検索処理＆結果の表示
        category_id = request.GET.get('c')
        keyword = request.GET.get('k')

        if category_id == "0":
            product_list = Product.objects.filter(name__icontains=keyword)
        else:
            product_list = Product.objects.filter(category_id=category_id, name__icontains=keyword)

        print(product_list[0].image.url)

        context = {
            "product_list": product_list,
            "keyword": keyword,
        }

        return render(request, "shop/product_search.html", context)


class ProductDetailView(View):
    def get(self, request, product_id):
        # 商品詳細ページの表示
        product = Product.objects.get(id=product_id)
        return render(request, "shop/product_detail.html", {"product": product})


class CartView(View):
    def get(self, request):
        # カートの表示
        cart_list = Cart.objects.prefetch_related("product_id").filter(user_id=request.user)

        # 在庫確認
        for item in cart_list:
            if item.product_id.stock < item.quantity or item.product_id.stock == 0:
                item.delete()
                cart_list = Cart.objects.prefetch_related("product_id").filter(user_id=request.user)

        # カート内の商品数
        cart_all_quantity = sum(item.quantity for item in cart_list)
        # カート内の合計金額
        total_price = sum(item.product_id.price * item.quantity for item in cart_list)

        context = {
            "cart_list": cart_list,
            "cart_all_quantity": cart_all_quantity,
            "total_price": total_price
        }

        return render(request, "shop/cart.html", context)


class CartAddView(View):
    def get(self, request, product_id):
        # カートに商品を追加する処理
        quantity = request.GET.get("q")

        # カートモデルにデータを登録
        cart_list = Cart.objects.filter(user_id=request.user, product_id=product_id)
        if cart_list.exists():
            # カートモデルに同じ商品が登録されている場合　→　個数が増える（更新）
            cart = cart_list.first()
            cart.quantity += quantity
            cart.save()

        else:
            # カートモデルに同じ商品が登録されていない場合　→　新規登録
            Cart.objects.create(
                user_id=request.user,
                product_id=Product.objects.get(id=product_id),
                quantity=quantity
            )

        return redirect("shop:cart")


index = IndexView.as_view()
product_search = ProductSearchView.as_view()
product_detail = ProductDetailView.as_view()
cart = CartView.as_view()
cart_add = CartAddView.as_view()
