from django.shortcuts import render
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
            product_list = Product.objects.filter(
                category_id=category_id, name__icontains=keyword)

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
        return render(
            request, "shop/product_detail.html", {"product": product})


class CartView(View):
    def get(self, request):
        # カートの表示
        pass


class CartAddView(View):
    def post(self, request, product_id):
        # カートに商品を追加する処理
        pass


index = IndexView.as_view()
product_search = ProductSearchView.as_view()
product_detail = ProductDetailView.as_view()
cart = CartView.as_view()
cart_add = CartAddView.as_view()
