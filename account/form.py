from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(label="帳號")
    password = forms.CharField(widget=forms.PasswordInput, label='密碼')
