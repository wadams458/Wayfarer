from django.db import models
# Import the User
from django.contrib.auth.models import User

# Create your models here.

#Profiles
class Profile(models.Model):
    city = models.CharField(max_length=100, blank=True)
    img = models.ImageField(upload_to='media/images/profiles', default='/static/images/default_profile.png') 
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    def __str__(self):
          return self.user.username

#Cities
class City(models.Model):
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    img = models.ImageField(upload_to='media/images/cities', default='/static/images/default_city.jpg') 

    def __str__(self):
        return self.name    

#Posts
class Post(models.Model):
    title = models.CharField(max_length=100)
    body = models.CharField(max_length=100000)
    img = models.ImageField(upload_to='media/images/posts', default='/static/images/default_post.jpg') 
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    
    def __str__(self):
      return self.title