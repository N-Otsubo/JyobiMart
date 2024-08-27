from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser


class LoginForm(forms.Form):
    username = forms.CharField(max_length=150, required=True)
    password = forms.CharField(widget=forms.PasswordInput, required=True)


class SignupForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = [
            'username',
            'password1',
            'password2',
            'email',
            'first_name',
            'last_name',
            'post_code',
            'address',
            'phone_number',
        ]
