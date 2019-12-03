from django.db import models
from .vendor import Vendor
from .user import UserInfo

class Member(models.Model):
  user = models.ForeignKey(
    UserInfo, 
    on_delete=models.CASCADE
  )
  vendor = models.ForeignKey(
    Vendor, 
    on_delete=models.CASCADE
  )
  company_role = models.CharField(max_length=100)

  # member fields are not included, only foerign keys 