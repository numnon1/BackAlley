from django.urls import path
from app import views

urlpatterns = [
    path('', views.play_game, name='play_game'),
]