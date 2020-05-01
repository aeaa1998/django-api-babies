from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
# Create your models here.

class Parent(models.Model):
   def json(self):
        return {
            "id" :self.id,
            'first_name': self.first_name,
            'last_name': self.last_name,
        }
   first_name = models.CharField(max_length=200)
   last_name = models.CharField(max_length=200)
   user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="parent")
   created_at = models.DateTimeField(default='2020-04-27 21:26:18.341835', blank=True)
   updated_at = models.DateTimeField(default='2020-04-27 21:26:18.341835', blank=True)

class Baby(models.Model):

   def json(self, withParent = False):
      json = {
         "id" :self.id,
         'first_name': self.first_name,
         'last_name': self.last_name,
      }
      if withParent:
         json["parent"] = self.parent
      return json
   first_name = models.CharField(max_length=200)
   last_name = models.CharField(max_length=200)
   parent = models.ForeignKey(Parent, on_delete=models.CASCADE, related_name="babies")
   
   class Meta:
      permissions = (
         ('see_baby', 'See baby'),
   )

