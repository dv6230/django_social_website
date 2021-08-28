from django.http import HttpResponse
from django.shortcuts import render

from django.contrib.auth import authenticate, login


def dashboard(request):
    return render(request, 'account/dashboard.html')
