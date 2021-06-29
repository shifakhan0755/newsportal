from django.db import models


# Create your models here.

class Main(models.Model):
    name = models.CharField(max_length=50)
    about = models.TextField()  # this is for footer  (default="-")
    profile_pic = models.ImageField(null=True,blank=True,upload_to='images/profile/')
    address = models.CharField(default="",max_length=500)  ## About page text
    fb = models.CharField(default="-", max_length=255,null=True,blank=True)
    tw = models.CharField(default="-", max_length=255,null=True,blank=True)
    yt = models.CharField(default="-", max_length=255,null=True,blank=True)
    tell = models.CharField(default="-", max_length=255)
    lin = models.CharField(default="-", max_length=255,null=True,blank=True)
    email = models.EmailField(default="-", max_length=255)


