from django.shortcuts import redirect
from django.template.response import TemplateResponse
from django.urls import reverse
from django.views import View
from .forms import SignUpForm


class SignupView(View):
    def get(self, request):
        form = SignUpForm()
        return TemplateResponse(request, "accounts/signup.html", {"form": form})

    def post(self, request):
        form = SignUpForm(request.POST)

        if form.is_valid():
            request.session['signup_form_data'] = form.cleaned_data
            return redirect("accounts:signup_confirm")

        print(form.errors)

        return TemplateResponse(request, "accounts/signup.html", {"form": form, "errors": form.errors})


class SignupConfirmView(View):
    def get(self, request):
        form_data = request.session.get('signup_form_data')

        if not form_data:
            return redirect("accounts:signup")

        # セッションからフォームデータを取得してテンプレートに渡します
        form = SignUpForm(initial=form_data)
        return TemplateResponse(request, "accounts/signup_confirm.html", {"form": form})

    def post(self, request):
        form_data = request.session.get('signup_form_data')
        if not form_data:
            return redirect("accounts:signup")

        form = SignUpForm(form_data)
        if form.is_valid():
            form.save()
            del request.session['signup_form_data']
            return redirect(reverse("login"))

        return redirect("accounts:signup", {"form": form, "errors": form.errors})


class ConfigView(View):
    def get(self, request):
        return TemplateResponse(request, "accounts/config.html")


signup = SignupView.as_view()
signup_confirm = SignupConfirmView.as_view()
config = ConfigView.as_view()