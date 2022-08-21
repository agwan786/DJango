from django.urls import path

from . import views

urlpatterns = [
    path('signup', views.signup, name='signup'),
    path('index', views.index, name='index'),
    path('adduser', views.adduser, name='adduser'),
]