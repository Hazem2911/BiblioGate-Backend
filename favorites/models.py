from django.db import models

class Favorites(models.Model) :
    user_id = models.ForeignKey('users.Users', on_delete=models.CASCADE)
    book_id= models.ForeignKey('books.Book', on_delete=models.CASCADE)




