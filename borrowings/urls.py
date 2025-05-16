from django.urls import path , include
from . import views
urlpatterns = [
path('borrow/', views.Borrowingsbooks.as_view(), name='borrow'),

]