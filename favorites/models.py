from django.conf import settings
from django.db import models

class Favorites(models.Model):
    favorite_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    book_id = models.ForeignKey('books.Book', on_delete=models.CASCADE)