from django.urls import path
from dashboard import views

urlpatterns = [
path('usersTable/', views.usersTable.as_view(), name='usersTable'),
path('borrowedBooksTable/', views.BorrowedBooksTable.as_view(), name='borrowedBooksTable'),
path('availableBooksTable/', views.AvailableBooksTable.as_view(), name='availableBooksTable'),
path('userBorrowedBooks/', views.UserBorrowedBooks.as_view(), name='userBorrowedBooks'),
path('latestBorrows/', views.LatestBorrowsTable.as_view(), name='latestBorrows'),
]