from django.db import models
from users.models import Users
# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=150)
    author = models.CharField(max_length=200)
    category = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    language = models.CharField(max_length=50 , default='English')
    image = models.CharField(max_length=1000)
    is_borrowed = models.BooleanField(default=False)
    user = models.ForeignKey(Users, on_delete=models.CASCADE, blank=True, null=True, related_name='books')
    user_favourite = models.ManyToManyField(Users, blank=True, related_name='favourites')