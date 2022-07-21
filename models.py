from django.db import models

# Create your models here.
class destination(models.Model):

    name= models.CharField(max_length=50)
    desc= models.TextField(max_length=100)
    image= models.ImageField(upload_to='pics') 
    price= models.IntegerField()
    offer= models.BooleanField(default=False)
    url= models.URLField(max_length=100)