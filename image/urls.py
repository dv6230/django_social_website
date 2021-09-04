from django.urls import path
from . import views

app_name = 'image'
urlpatterns = [
    path('upload/', views.image_upload, name='image_upload'),
    path('list/', views.image_list, name='image_list'),
    path('<int:id>/', views.image_detail, name='image_detail'),
    path('like/<int:id>', views.image_like, name='image_like'),
    path('dislike/<int:id>', views.image_dislike, name='image_dislike'),

]
