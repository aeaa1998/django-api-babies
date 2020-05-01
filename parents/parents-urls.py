from django.urls import path
from . import views

urlpatterns = [
    path('<str:id>/babies', views.index, name = 'index')
]