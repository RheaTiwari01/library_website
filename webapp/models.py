from django.db import models

# Create your models here.


class Author(models.Model):
    fname = models.CharField(max_length=200)
    lname = models.CharField(max_length=200)
    email=models.EmailField()
    def __str__(self):
        return f"{self.fname} {self.lname}"

class Publisher(models.Model):
    name= models.CharField(max_length=200)
    country = models.CharField(max_length=100)
    website = models.URLField()

    def __str__(self):
        return self.name
    
class Book(models.Model):
    title=models.CharField(max_length=200)
    publish_date = models.DateField()
    author = models.ManyToManyField(Author)
    publisher=models.ForeignKey(Publisher,on_delete=models.CASCADE)
    def __str__(self):
        return self.title
