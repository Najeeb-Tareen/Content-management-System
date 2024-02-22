from django.db import models


# Create your models here.


class Person(models.Model):
    username = models.CharField(max_length=64)
    email = models.EmailField(max_length=64)
    age = models.IntegerField()

    def __str__(self):
        return self.username
    



class Categories(models.Model):
    name = models.CharField(max_length=255)
    typi = models.CharField(max_length=255)
     
    def __str__(self):
        return self.name
    

class Article(models.Model):
    title = models.CharField(max_length= 128)
    content = models.CharField(max_length= 128)
    publication_date = models.DateTimeField(auto_now=True)
    category = models.ManyToManyField(Categories, null=True, blank=True)


    def __str__(self):
        return self.title
    







    
   

    

