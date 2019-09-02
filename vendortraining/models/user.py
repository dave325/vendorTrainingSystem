from django.db import models
from .role import Role
from .event import Event
class UserInfo(models.Model):
  role = models.ForeignKey(
    Role, 
    on_delete=models.CASCADE)
  phone = models.CharField(max_length=100)
  address = models.CharField(max_length=254)
  public = models.BooleanField(default=True)
  #events = models.ManyToManyField(Event, through=u'Attendance')


