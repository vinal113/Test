from django.db import models
import uuid
from django.contrib.auth import get_user_model  
  
User = get_user_model()  

#Profile Model
class Profile(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, null= True, default= "Anonymous User")
    profile_pic = models.ImageField(upload_to='media/pic')
    bio = models.TextField()


class Category(models.Model):
    name = models.CharField(max_length=50,editable=False, primary_key=True)

# Posts Model
class PostsModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    media = models.FileField(upload_to='media/feed')
    caption = models.CharField(max_length=4000)
    likes = models.IntegerField(default=0)
    price = models.FloatField(default=0)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    results = models.TextField()
    catagory = models.ForeignKey(Category, on_delete=models.CASCADE)
    baught_by = models.IntegerField(default=0)
