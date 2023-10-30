from django.db import models

# Create your models here.


class Record(models.Model):
    
    first_name=models.CharField(max_length=70)
    last_name=models.CharField(max_length=70)
    email=models.CharField(max_length=70)
    address=models.CharField(max_length=70)
    profile_imagee=models.ImageField(null=True,blank=True,upload_to='images/')