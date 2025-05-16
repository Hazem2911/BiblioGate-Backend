from django.db import models

# Create your models here.
class borrowings (models.Model):
    user_id = models.ForeignKey('users.Users' , on_delete=models.CASCADE)
    book_id = models.ForeignKey('books.Book' , on_delete=models.CASCADE)