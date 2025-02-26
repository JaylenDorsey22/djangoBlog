from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length= 100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete= models.CASCADE)
    
    
    def __str__(self):
        return self.title
    
class Users(models.Model):
    username = models.CharField(User, max_length = 20)
    email = models.EmailField(max_length=100)
    password = models.CharField(User, max_length=30)





    



