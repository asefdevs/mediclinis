from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    picture=models.ImageField(blank=True,null=True,upload_to='user_picture')
    location = models.CharField(max_length=30, blank=True)
   