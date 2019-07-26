from django.db import models
from django.utils import timezone
from .vendor import Vendor
from .user import User

class Event(models.Model):
  vendor_id = models.ForeignKey(
    Vendor,
    related_name="vendor_name",
    on_delete=models.CASCADE
  )
  created_by = models.CharField(max_length=100)
  created_at = models.DateField(auto_now_add=True)
  modified_by = models.ForeignKey(
    User,
    on_delete=models.CASCADE
  )
  modified_at = models.DateField(auto_now=True)