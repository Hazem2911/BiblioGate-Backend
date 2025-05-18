from django.contrib.auth.models import AbstractUser
from django.db import models

class Users(AbstractUser):
    username = models.CharField(max_length = 100 , unique = True)
    email = models.EmailField(max_length = 100 , unique = True)
    password = models.CharField(max_length = 30)
    total_borrowings = models.IntegerField(default=0)
    total_returns = models.IntegerField(default=0)
    is_staff = models.BooleanField(default=False)




