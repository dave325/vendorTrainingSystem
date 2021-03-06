from django.db import models

class Vendor(models.Model):
  name = models.CharField(max_length=100) 
  address = models.CharField(max_length=100) 
  phone = models.CharField(max_length=100) 
  email = models.EmailField(max_length=254)
  is_approved = models.BooleanField(default=False)