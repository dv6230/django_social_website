from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login, password_validation
from django.contrib.auth.forms import UserCreationForm
from .form import LoginForm , MyUserCreationForm
import django.forms


def dashboard(request):
    return render(request, 'account/dashboard.html')


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(
                request, username=cd['username'], password=cd['password']
            )
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse(
                        'Authenticate successfully'
                    )
                else:
                    return HttpResponse('Disabled acccount')
            else:
                return HttpResponse('Invalid login')
    else:
        form = LoginForm()
        return render(request, 'account/login.html', {'form': form})


def register(request):
    if request.method == 'POST':
        user_form = MyUserCreationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(
                user_form.cleaned_data['password1']
            )
            new_user.save()
            return render(
                request,
                'account/register_done.html',
                {'new_user': new_user}
            )
    else:
        user_form = MyUserCreationForm()

    return render(request, 'account/register.html', {'user_form': user_form})
