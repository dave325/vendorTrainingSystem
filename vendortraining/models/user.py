from django.db import models
from .role import Role

class User(models.Model):
  id = models.IntegerField(primary_key=True) 
  email = models.CharField(max_length=100)
  first_name = models.CharField(max_length=100)
  last_name = models.CharField(max_length=100)
  role_id = models.ForeignKey(
    Role, 
    on_delete=models.CASCADE)
  phone = models.CharField(max_length=100)
  address = models.TextField()
  public = models.BooleanField(default=True)
  password = models.CharField(max_length=100)