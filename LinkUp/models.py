from django.db import models
from django.contrib.auth.models import User
import uuid 
from datetime import datetime

class Profile(models.Model):
  user = models.ForeignKey(User,on_delete=models.CASCADE)
  id_user = models.IntegerField(primary_key=True,default=0) 
  bio = models.TextField(blank=True,default='')
  profile_img = models.ImageField(upload_to='profile_images',default='https://tse2.mm.bing.net/th?id=OIG4.xDrW4Yp4C8ElAsk2hZSZ&w=270&h=270&c=6&r=0&o=5&pid=ImgGn')
  location = models.CharField(max_length=300,blank=True,default='')
  
  def __str__(self):
    return f'{self.user.username} - {self.bio[:20]}'
  

class Post(models.Model):
  id = models.UUIDField(primary_key=True,default=uuid.uuid4)
  user = models.CharField(max_length=200)
  image = models.ImageField(upload_to='post_images')
  caption = models.TextField()
  created_at = models.DateTimeField(default=datetime.now)
  no_of_likes = models.IntegerField(default=0)
  
  def __str__(self):
    return f'Post by {self.user}'
  
class LikePost(models.Model):
  post_id = models.CharField(max_length=500)
  username = models.CharField(max_length=100)

  def __str__(self):
    return self.username
  
class Follower(models.Model):
  follower = models.CharField(max_length=300)
  user = models.CharField(max_length=100)
  
  def __str__(self):
    return f'{self.follower} follows {self.user}'
    
