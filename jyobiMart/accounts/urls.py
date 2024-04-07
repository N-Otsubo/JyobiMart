from django.urls import path
from . import views

app_name = "accounts"
urlpatterns = [
    path("signup/", views.signup, name="signup"),
    path("signup/confirm", views.signup_confirm, name="signup_confirm"),
    path("config/", views.config, name="config"),
]
