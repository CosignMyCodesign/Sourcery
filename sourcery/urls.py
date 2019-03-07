from django.conf.urls import url
from django.urls import path

from . import views

app_name = "sourcery"
urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login_user, name='login'),
    path('logout', views.user_logout, name='logout'),
    path('register', views.register, name='register'),
    path('resources/', views.resourceGrid, name='resourceGrid')
]