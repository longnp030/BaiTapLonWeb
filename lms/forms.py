from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _


class RegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

    username = forms.CharField(label=_('Tên đăng nhập'))
    password1 = forms.CharField(label=_('Mật khẩu'))
    password2 = forms.CharField(label=_('Nhập lại mật khẩu'))