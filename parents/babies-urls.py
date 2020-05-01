from django.urls import path
from . import views

urlpatterns = [
    path('<str:id>', views.babyById, name ='babyById'),
    path('<str:id>/events', views.eventsByBabyId, name ='eventsByBabyId'),
    path('', views.storeBaby, name ='storeBaby')
]