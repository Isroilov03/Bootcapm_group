from django.db import models

# Create your models here.

class Book(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField()



class Notbuk(models.Model):
    name = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
