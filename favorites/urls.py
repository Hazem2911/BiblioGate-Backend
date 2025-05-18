from django.urls import path , include
from . import views


urlpatterns = [
    path('add_to_fav/', views.AddToFavourites.as_view(), name='addtofav'),
    path('get_favs/', views.GetFavourites.as_view(), name='get_favs'),
    path('remove_fav/', views.RemoveFromFavourites.as_view(), name='remove_fav'),
]