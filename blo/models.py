from django.db import models
from django.conf import settings
# Create your models here.

class Books(models.Model):
    b_id=models.IntegerField()
    b_name=models.CharField(max_length=100)
    b_author=models.CharField(max_length=100)
    b_publisher=models.CharField(max_length=100)
    b_year=models.IntegerField()
    b_img_src=models.CharField(max_length=100)
    b_describe=models.CharField(max_length=2000)
