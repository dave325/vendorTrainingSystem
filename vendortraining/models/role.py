from django.db import models

class Role(models.Model):
  role_name = models.CharField(max_length=100)