from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
# Create your models here.

class Books(models.Model):
    b_id=models.IntegerField()
    b_name=models.CharField(max_length=100)
    b_author=models.CharField(max_length=100)
    b_publisher=models.CharField(max_length=100)
    b_year=models.IntegerField()
    b_img_src=models.CharField(max_length=100)
    b_describe=models.CharField(max_length=2000)
'''
class CustomUser(models.Model):
    username=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    #password=models.CharField(max_length=100)

    def __str__(self):
        return self.email

class UserProfileInfo(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    portfolio_site = models.URLField(blank=True)
    #profile_pic = models.ImageField(upload_to='profile_pics',blank=True)
    def __str__(self):
          return self.user.username
'''
