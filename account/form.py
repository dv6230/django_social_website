from django import forms
from django.contrib.auth import password_validation
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class LoginForm(forms.Form):
    username = forms.CharField(label="帳號")
    password = forms.CharField(widget=forms.PasswordInput, label='密碼')


class MyUserCreationForm(UserCreationForm):
    password1 = forms.CharField(
        label="密碼",
        error_messages={
            'required': '必要',
        },
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )
    password2 = forms.CharField(
        label="密碼確認",
        error_messages={
            'required': '必要',
        },
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )
    error_messages = {
        'password_mismatch': "兩者密碼不相同",
    }

    class Meta:
        model = User
        fields = ("username", "first_name", "last_name", "email", "password1", "password2")
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
                'invalid': '請檢查輸入內容是否正確',
                'password_mismatch': "test content",
            },
            'password_mismatch': ("test content"),
        }
