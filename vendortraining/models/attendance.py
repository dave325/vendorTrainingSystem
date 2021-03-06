from django.db import models
from .event import Event
from .user import UserInfo

class Attendance(models.Model):
  event = models.ForeignKey(
    Event, 
    on_delete=models.CASCADE
  )