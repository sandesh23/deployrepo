from django.db import models

# Create your models here.
class Address(models.Model):
    id = models.AutoField(primary_key=True)
    area = models.TextField(max_length=100,null= False)
    city = models.CharField(max_length=100)
    state=models.CharField(max_length=100)
    country=models.CharField(max_length=100)

