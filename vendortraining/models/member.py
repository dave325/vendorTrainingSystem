from django.db import models
from .vendor import Vendor
from .user import User

class Member(models.Model):
  user_id = models.ForeignKey(
    User, 
    on_delete=models.CASCADE
  )
  vendor_id = models.ForeignKey(
    Vendor, 
    on_delete=models.CASCADE
  )
  company_role = models.CharField(max_length=100)