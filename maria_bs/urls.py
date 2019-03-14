"""Определяет схемы URL для maria_bs."""
from django.urls import path
from . import views

app_name = 'maria_bs'
urlpatterns = [
    # Домашняя страница
    path('', views.index, name='index'),
]
