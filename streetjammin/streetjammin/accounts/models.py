from django.conf import settings
from django.db import models
from django.utils import timezone
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class Musician(models.Model):
  mid = models.BigIntegerField(primary_key=True)
  username = models.CharField(max_length=30, unique = True)

class Songs(models.Model):
  mid = models.BigIntegerField(primary_key=True)
  sid = models.BigIntegerField()
  username = models.CharField(max_length=30, unique = True)
  published = models.DateTimeField(default=timezone.now)
  dl_count = models.PositiveIntegerField()
  last_dl = models.DateTimeField(auto_now=True)

  class Meta:
    unique_together = (('mid','sid'),) #logically, Songs are nested under Musicians


class Downloads(models.Model):
  sid = models.BigIntegerField(primary_key = True)
  did = models.BigIntegerField()
  mid = models.ForeignKey(Musician, on_delete=models.CASCADE)
  state = models.BooleanField(default = False) # False = Not downloaded; True = Downloaded

  class Meta:
    unique_together = (('sid','did'),) #logically, Downloads are nested under Songs, which are nested under Musicians




