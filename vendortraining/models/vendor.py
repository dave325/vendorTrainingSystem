from django.db import models

class Vendor(models.Model):
  vendor_id = models.IntegerField(primary_key=True) 
  name = models.CharField(max_length=100) 
  address = models.TextField()
  phone = models.CharField(max_length=100) 
  email = models.EmailField(max_length=254)
  is_approved = models.BooleanField(default=False)