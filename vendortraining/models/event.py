from django.db import models
from django.utils import timezone
from .vendor import Vendor
from .user import User

class Event(models.Model):
  vendor_id = models.ForeignKey(
    Vendor,
    on_delete=models.CASCADE
  )
  created_by = models.ForeignKey(
    Vendor,
    related_name='created_by',
    on_delete=models.CASCADE
  )
  created_at = models.DateField(auto_now_add=True)
  modified_by = models.ForeignKey(
    User,
    related_name='modified_by',
    on_delete=models.CASCADE
  )
  modified_at = models.DateField(auto_now=True)
