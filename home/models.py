from django.db import models
from django.utils.html import format_html
from taggit.managers import TaggableManager
from ckeditor.fields import RichTextField
from django.db.models.signals import pre_save
from newsportal11.utils import unique_slug_generator



# Create your models here.
Entertainment_CHOICES = (
    ('B','bollywood'),
    ('H','hollywood'),
    ('T','television'),
)

class EntertainmentModel(models.Model):
    title =models.CharField(max_length=100,blank=True)
    slug = models.SlugField(null=True, max_length=500, blank=True)
    caption =models.CharField(max_length=1000,blank=True)
    d_description = RichTextField(blank=True)
    date = models.DateTimeField(auto_now_add=True,blank=True)
    description = RichTextField(blank=True)
    category = models.CharField(choices=Entertainment_CHOICES,max_length=2)
    s_image = models.ImageField(upload_to='producting',blank=True,null=True)
    s_vedio = models.FileField(upload_to='vedio/%y', blank=True)
    a = models.SlugField(unique=True,null=True,max_length=100, blank=True)

    tags = TaggableManager()



def slug_generator(sender,instance,*args,**kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)
pre_save.connect(slug_generator,sender=EntertainmentModel)

Corona_CHOICES = (
    ('V','vaccine'),
    ('D','death'),
    ('R','recovered'),
)
class CoronaModel(models.Model):
    title =models.CharField(max_length=100,blank=True)
    slug = models.SlugField(null=True, max_length=500, blank=True)
    caption =models.CharField(max_length=100,blank=True)
    d_description = RichTextField(blank=True)
    date = models.DateTimeField(auto_now_add=True,blank=True)
    description = RichTextField(blank=True)
    category = models.CharField(choices=Corona_CHOICES,max_length=2)
    tags = TaggableManager()
    s_image = models.ImageField(upload_to='producting',blank=True)
    s_vedio = models.FileField(upload_to='vedio/%y', blank=True)
def slug_generator2(sender,instance,*args,**kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)
pre_save.connect(slug_generator2,sender=CoronaModel)

CATEGORY_CHOICES = (
    ('N','ncr'),
    ('UP','uttar pradesh'),
    ('B','bihar'),
    ('UK','uttarakhand'),
    ('J', 'jharkhand'),
    ('R', 'rajasthan'),
    ('MP', 'madhya pradesh'),
    ('M', 'maharashtra'),
    ('H', 'haryana'),
    ('CH', 'chhattisgarh'),
    ('HP', 'himachal pradesh'),
)

class StateModel(models.Model):
    title =models.CharField(max_length=100)
    slug = models.SlugField(null=True, max_length=500, blank=True)
    caption =models.CharField(max_length=100,blank=True)
    detail_description = RichTextField(blank=True)
    date = models.DateTimeField(auto_now_add=True)
    description = RichTextField(blank=True)
    category = models.CharField(choices=CATEGORY_CHOICES,max_length=2)
    tags = TaggableManager()
    s_image = models.ImageField(upload_to='producting')
    s_vedio = models.FileField(upload_to='vedio/%y', blank=True)
def slug_generator11(sender,instance,*args,**kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)
pre_save.connect(slug_generator11,sender=StateModel)

class IPLModel(models.Model):
    title = models.CharField(max_length=100,blank=True)
    slug = models.SlugField(null=True, max_length=500, blank=True)
    caption = models.CharField(max_length=500,blank=True)
    detail_description = RichTextField(blank=True)
    date = models.DateTimeField(auto_now_add=True,blank=True)
    description = RichTextField(blank=True)
    tags = TaggableManager()
    s_image = models.ImageField(upload_to='producting',blank=True)
    s_vedio = models.FileField(upload_to='vedio/%y', blank=True)

def slug_generator14(sender,instance,*args,**kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)
pre_save.connect(slug_generator14,sender=IPLModel)


Career_CHOICES = (
    ('E','education'),
    ('BR','board results'),
    ('A','admission'),
)

class CareerModel(models.Model):
    title =models.CharField(max_length=100,blank=True)
    slug = models.SlugField(null=True, max_length=500, blank=True)
    caption =models.CharField(max_length=500,blank=True)
    detail_description =  RichTextField(blank=True)
    date = models.DateTimeField(auto_now_add=True,blank=True)
    description = RichTextField(blank=True)
    category = models.CharField(choices=Career_CHOICES,max_length=2)
    tags = TaggableManager()
    s_image = models.ImageField(upload_to='producting',blank=True)
    s_vedio = models.FileField(upload_to='vedio/%y', blank=True)


def slug_generator13(sender,instance,*args,**kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)
pre_save.connect(slug_generator13,sender=CareerModel)

class WorldModel(models.Model):
    title =models.CharField(max_length=100,blank=True)
    slug = models.SlugField(null=True, max_length=500, blank=True)
    caption =models.CharField(max_length=100,blank=True)
    detail_description = RichTextField(blank=True)
    date = models.DateTimeField(auto_now_add=True,blank=True)
    description = RichTextField(blank=True)
    tags = TaggableManager()
    s_image = models.ImageField(upload_to='producting',blank=True)
    s_vedio = models.FileField(upload_to='vedio/%y', blank=True)

def slug_generator3(sender,instance,*args,**kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)
pre_save.connect(slug_generator3,sender=WorldModel)

class ContactModel(models.Model):
    name = models.CharField(max_length=70)
    email = models.EmailField(max_length=150)
    subject = models.TextField(max_length=100,blank=True)
    comment = models.TextField(max_length=2000)

News_CHOICES = (
    ('B','breaking'),
    ('L','latest'),
)

class News(models.Model):
    title =models.CharField(max_length=100,blank=True)
    caption =models.CharField(max_length=100,blank=True)
    d_description = models.TextField(blank=True)
    date = models.DateTimeField(auto_now_add=True,blank=True)
    description = models.TextField(blank=True)
    category = models.CharField(choices=News_CHOICES, max_length=2)
    s_image = models.ImageField(upload_to='producting',blank=True)
    s_vedio = models.FileField(upload_to='vedio/%y', blank=True)

    def __str__(self):
        return str(self.id)
