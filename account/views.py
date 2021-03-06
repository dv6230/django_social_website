from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, password_validation
from django.contrib.auth.forms import UserCreationForm
from .form import LoginForm, MyUserCreationForm
import django.forms
from django.contrib.auth import authenticate, login
from .models import Contract


@login_required(login_url='/account/login/')
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


@login_required()
def profile(request, username):
    user = User.objects.filter(username=username).first()
    if user is not None:
        return render(request, 'account/profile.html', {'user': user})
    else:
        return redirect('/account/')


@login_required()
def user_list(request):
    user_list = User.objects.all()
    return render(request, 'account/user_list.html', {'users': user_list})


@login_required()
def follow(request, username):
    user_to = User.objects.filter(username=username).first()
    user_from = request.user
    contract = Contract(
        user_from=user_from,
        user_to=user_to
    )
    contract.save()
    return redirect('profile', username=username)


@login_required()
def unfollow(request, username):
    user_to = User.objects.filter(username=username).first()
    user_from = request.user
    con = Contract.objects.filter(user_from=user_from, user_to=user_to).first()
    if con:
        con.delete()
    return redirect('profile', username=username)

# def (reabc123quest):
#     return JsonResponse({'status': 'scuuess'})
