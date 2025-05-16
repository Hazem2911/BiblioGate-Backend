from django.db import models

from Backend import settings


# Create your models here.
class borrowings(models.Model):
    borrowings_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    book = models.ForeignKey('books.Book', on_delete=models.CASCADE)
