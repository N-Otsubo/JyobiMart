from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from django.contrib.auth import login, logout, authenticate
from .forms import LoginForm


# Create your views here.
# ログイン
class LoginView(View):
    def get(self, request):
        # ログイン画面テンプレートの表示
        form = LoginForm()
        return render(request, 'account/login.html', {"form": form})

    def post(self, request, *args, **kwargs):
        # ログイン処理
        form = LoginForm(request.POST)

        if not form.is_valid():
            return render(request, 'account/login.html', {'form': form})

        username = form.cleaned_data['username']
        password = form.cleaned_data['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect(reverse("shop:index"))

        return render(request, 'account/login.html', {'form': form})


# ログアウト
class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect(reverse('account:user_login'))


# 新規登録
class SigninView(View):
    def get(self, request):
        # 新規登録画面テンプレートを表示
        pass

    def post(self, request, *args, **kwargs):
        # 登録処理
        pass


# ビュークラスのインスタンス化
user_login = LoginView.as_view()
user_logout = LogoutView.as_view()
signin = SigninView.as_view()
