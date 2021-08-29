from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class LoginForm(forms.Form):
    username = forms.CharField(label="帳號")
    password = forms.CharField(widget=forms.PasswordInput, label='密碼')


class MyUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username", "first_name", "last_name", "email")
        labels = {
            'username': '暱稱',
            'email': '電子郵件',
            'first_name': '姓氏',
            'last_name': '名稱',
            'password1': '密碼',
            'password2': '再次輸入密碼',
        }
        error_messages = {
            '__all__': {
                'required': '請輸入內容',
                'invalid': '請檢查輸入內容是否正確'
            },
        }
