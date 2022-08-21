from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login', views.as_view, name='login'),
    path('add', views.add, name='add')
]