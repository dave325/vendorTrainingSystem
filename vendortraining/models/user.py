from django.db import models
from .role import Role
from .event import Event
from django.contrib.auth.models import User
class UserInfo(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  role = models.ForeignKey(
    Role, 
    on_delete=models.CASCADE)
  phone = models.CharField(max_length=100)
  address = models.CharField(max_length=254)
  public = models.BooleanField(default=True)
  #events = models.ManyToManyField(Event, through=u'Attendance')


