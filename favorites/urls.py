from django.urls import path , include
from . import views


urlpatterns = [
    path('addfavorites/', views.AddFavorites.as_view(), name='addfavorites'),

    path('getfavorites/', views.GetFavorites.as_view(), name='getfavorites'),

    path('deletefavorites/', views.DeleteFavorites.as_view(), name='deletefavorites'),
]