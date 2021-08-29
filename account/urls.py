from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

# LoginView = auth_views.LoginView
# LoginView.as_view(template_name='registration/login2.html')

urlpatterns = [
    # path('login/', views.user_login, name='login'),
    path('login/', auth_views.LoginView.as_view(template_name='account/login.html'), name='login'),
    path('', views.dashboard, name='dashboard'),
    path('register/',views.register,name='register'),
]
