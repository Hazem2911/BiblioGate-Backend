from django.urls import path , include
from . import views
urlpatterns = [
path('borrow_book/', views.BorrowBook.as_view(), name='borrow'),
path('borrowed_books/', views.GetBorrowings.as_view(), name='borrowed'),
path('return_book/', views.ReturnBook.as_view(), name='return'),
]