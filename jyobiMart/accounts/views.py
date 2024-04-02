from django.views import View
from django.contrib.auth.views import LoginView
from django.template.response import TemplateResponse

# Create your views here.
class LoginView(LoginView):
    template_name = "accounts/login.html"

class SignupView(View):
    def get(self, request):
        return TemplateResponse(request, "accounts/signup.html")

signup = SignupView.as_view()
