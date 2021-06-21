from django.db import models


# Create your models here.

class Main(models.Model):
    name = models.CharField(max_length=50)
    about = models.TextField()  # this is for footer  (default="-")
    address = models.CharField(default="",max_length=500)  ## About page text
    fb = models.CharField(default="-", max_length=50)
    tw = models.CharField(default="-", max_length=50)
    yt = models.CharField(default="-", max_length=50)
    tell = models.CharField(default="-", max_length=50)
    lin = models.CharField(default="-", max_length=50)
    email = models.EmailField(default="-", max_length=50)


