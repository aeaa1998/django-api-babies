from django.urls import path
from . import views

urlpatterns = [
    path('', views.store, name ='store'),
    path('<str:id>', views.eventById, name ='eventById')
]