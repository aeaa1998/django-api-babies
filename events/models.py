from django.db import models
from parents.models import Baby

# Create your models here.

class Type(models.Model):
   name = models.CharField(max_length=200)

class Event(models.Model):
   def json(self, withBaby = False):
      json = {
         "id" :self.id,
         "comment" : self.comment,
         "event_type" : self.event_type.name
      }
      if(withBaby):
         json["baby"] = self.baby.json()
      return json
   comment = models.CharField(max_length=200)
   event_type = models.ForeignKey(Type, on_delete=models.CASCADE)
   baby = models.ForeignKey(Baby, on_delete=models.CASCADE)
   class Meta:
      permissions = (
         ('see_event', 'See event'),
   )