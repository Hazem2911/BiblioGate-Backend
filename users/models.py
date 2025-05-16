from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here

# class User (AbstractUser):
#     fav_books = models.ManyToManyField("user.Book" , related_name='users' , blank=True)
#
#
# class Book(models.Model):
#    name = models.CharField(max_length=50)
#     title = models.CharField(max_length=50)
#
#     borrowed_by = models.ForeignKey(User, on_delete=models.CASCADE , blank=True, null=True)
#
#     def __str__(self):
#         return self.name + " " + self.title


class Users(AbstractUser):
    username = models.CharField(max_length = 100 , unique = True)
    email = models.EmailField(max_length = 100 , unique = True)
    password = models.CharField(max_length = 30)
    total_borrowings = models.IntegerField(default=0)
    total_returns = models.IntegerField(default=0)
    is_staff = models.BooleanField(default=False)


