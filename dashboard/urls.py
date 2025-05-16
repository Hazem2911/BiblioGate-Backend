from django.urls import path

from dashboard import views

urlpatterns = [

path('usersTable/', views.usersTable.as_view(), name='usersTable'),
]