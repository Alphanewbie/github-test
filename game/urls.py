from django.urls import path
from . import views

app_name = 'game'
urlpatterns = [
    path('mine/', views.game, name = 'mine'),
]