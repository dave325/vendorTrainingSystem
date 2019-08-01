from django.db import models
from .role import Role
from .event import Event

class User(models.Model):
  email = models.CharField(max_length=100)
  first_name = models.CharField(max_length=100)
  last_name = models.CharField(max_length=100)
  role_id = models.ForeignKey(
    Role, 
    on_delete=models.CASCADE)
  phone = models.CharField(max_length=100)
  address = models.CharField(max_length=254)
  public = models.BooleanField(default=True)
  password = models.CharField(max_length=100)
  events = models.ManyToManyField(Event, through=u'Attendance')