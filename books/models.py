from django.db import models

# Create your models here.
# -- Books table
# CREATE TABLE Books (
#     book_id INT IDENTITY(1,1) PRIMARY KEY,
#     title VARCHAR(150) NOT NULL,
#     author VARCHAR(200) NOT NULL,
#     category VARCHAR(100) NOT NULL,
#     description VARCHAR(200) NOT NULL,
#     cover_image VARCHAR(500) Not Null
# );



class Book(models.Model):
    title = models.CharField(max_length=150)
    author = models.CharField(max_length=200)
    category = models.CharField(max_length=100)
    language = models.CharField(max_length=50 , default='English')
    description = models.CharField(max_length=200)
    cover_image = models.CharField(max_length=1000)
    is_borrowed = models.BooleanField(default=False)
