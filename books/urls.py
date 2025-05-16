from django.urls import path , include
from . import views
urlpatterns = [
path('addbook/', views.AddBook.as_view(), name='addbook'),
path('getbook/', views.GetBook.as_view(), name='getbook'),

path('deletebook/', views.DeleteBook.as_view(), name='deletebook'),
]

# baseurl books/AddBook/