from django.db import models

class Vendor(models.Model):
  name = models.CharField(max_length=100) 
  address = models.TextField()
  phone = models.CharField(max_length=100) 
  email = models.EmailField(max_length=254)