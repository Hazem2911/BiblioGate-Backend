from django.urls import path , include
from . import views
from .views import Login

urlpatterns = [
path('login/', Login.as_view(), name='login'),
path('register/', views.Register.as_view(), name='register'),
]
