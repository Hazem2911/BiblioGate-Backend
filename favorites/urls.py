# favorites/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('addfavorites/', views.add_favorite, name='add_favorite'),
    path('deletefavorites/', views.delete_favorite, name='delete_favorite'),
    path('getfavorites/', views.get_favorites, name='get_favorites'),
]
