from django.conf.urls import url
from django.urls import path

from . import views

app_name = "sourcery"
urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login_user, name='login'),
    path('logout', views.user_logout, name='logout'),
    path('register', views.register, name='register'),
    path('resources/<int:resource_type_id>/<int:user_id>/', views.resourceGrid, name='resourceGrid'),
    path('addResourceType', views.addResourceType, name='addResourceType'),
    path('addResource', views.addResource, name='addResource'),
    path('resourceForm', views.resourceForm, name='resourceForm'),
]