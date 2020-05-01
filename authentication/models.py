from django.db import models
from datetime import datetime
# Create your models here.

class User(models.Model):
   email = models.CharField(max_length=200, unique = True)
   password = models.CharField(max_length=200)
   created_at = models.DateTimeField(default=datetime.now, blank=True)
   updated_at = models.DateTimeField(default=datetime.now, blank=True)
   def __str__(self):
        return self.email
