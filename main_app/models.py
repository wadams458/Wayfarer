from django.db import models
# Import the User
from django.contrib.auth.models import User

# Create your models here.

#Profiles
class Profile(models.Model):
    city = models.CharField(max_length=100)
    img = models.CharField(max_length=300, blank=True, null=True)
    # user = models.CharField(max_length=100)


#Posts
class Post(models.Model):
    title = models.CharField(max_length=100)
    body = models.CharField(max_length=100000)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # city = models.CharField(max_length=100)

#Cities
class City(models.Model):
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    img = models.CharField(max_length=300)
    # posts = models.CharField(max_length=100)
    
