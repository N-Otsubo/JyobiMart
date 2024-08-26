from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from django.contrib.auth import login, logout, authenticate
from .forms import LoginForm, SignupForm


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
class SignupView(View):
    def get(self, request):
        # 新規登録画面テンプレートを表示
        form = SignupForm()
        return render(request, 'account/signup.html', {'form': form})

    def post(self, request, *args, **kwargs):
        # 確認画面への遷移
        form = SignupForm(request.POST)

        if form.is_valid():
            request.session['signup_data'] = form.cleaned_data
            return redirect('account:signup_confirm')
        
        return render(request, 'account/signup.html', {'form': form})


class SignupConfirmView(View):
    def get(self, request):
        # 確認画面の表示
        form_data = request.session.get('signup_data')
        if not form_data:
            return redirect('account:signup')

        form = SignupForm(initial=form_data)
        return render(request, 'account/signup_confirm.html', {'form': form})

    def post(self, request, *args, **kwargs):
        # 登録処理
        form_data = request.session.get('signup_data')
        if not form_data:
            return redirect('account:signup')

        form = SignupForm(form_data)
        if form.is_valid():
            form.save()
            del request.session['signup_data']
            return redirect("account:user_login")

        return redirect("account:signup")


# ビュークラスのインスタンス化
user_login = LoginView.as_view()
user_logout = LogoutView.as_view()
signup = SignupView.as_view()
signup_confirm = SignupConfirmView.as_view()
