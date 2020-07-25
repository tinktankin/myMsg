from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Social(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    facebook_link = models.CharField(max_length=100,blank=True)
    linkedin_link = models.CharField(max_length=100,blank=True)
    twitter_link = models.CharField(max_length=100,blank=True)

