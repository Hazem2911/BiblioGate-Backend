from django.urls import path , include
from . import views
urlpatterns = [
path('addbook/', views.AddBook.as_view(), name='addbook'),
path('getbook/', views.GetBook.as_view(), name='getbook'),
path('editbook/', views.EditBook.as_view(), name='editbook'),
path('deletebook/', views.DeleteBook.as_view(), name='deletebook'),
]
