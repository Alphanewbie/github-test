from django.urls import path
from . import views

app_name = 'game'
urlpatterns = [
    path('mine/', views.mine, name = 'mine'),
    path('mine/<int:y>/<int:x>/search-mine/', views.search_mine, name = 'search_mine'),
    path('mine/<int:y>/<int:x>/flag-evnet/', views.flag_evnet, name = 'flag_evnet'),
]