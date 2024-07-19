from .models import Category, Cart


class HeaderMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # カテゴリーモデルからデータを取得する
        request.categories = Category.objects.all()
        
        # カートモデルからデータを取得する
        if request.user.is_authenticated:
            request.cart_count = Cart.objects.filter(user_id=request.user).count()

        response = self.get_response(request)
        return response
