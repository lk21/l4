from django.db import models
1 change
class Author(models.Model):
    authorID = models.CharField(max_length=20,primary_key=True)
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    country = models.CharField(max_length=30)
    
    
class Book(models.Model):
    isbn = models.CharField(max_length=13, primary_key=True)
    title = models.CharField(max_length=50)
    authorID = models.ForeignKey(Author)
    publisher = models.CharField(max_length=30)
    publishDate = models.DateField()
    price = models.CharField(max_length=6)


