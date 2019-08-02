from django.db import models
from .event import Event
from .user import User

class Attendance(models.Model):
  event = models.ForeignKey(
    Event, 
    on_delete=models.CASCADE
  )
  user = models.ForeignKey(
    User, 
    on_delete=models.CASCADE
  )