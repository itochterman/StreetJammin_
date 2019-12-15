from django.db import models
from django import forms

# Create your models here.
# can test inside: inside venv, use python3 manage.py shell


from django.conf import settings
from django.db import models
from django.utils import timezone
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
import datetime

class Musicians(models.Model):
  mid = models.AutoField(primary_key=True)
  username = models.CharField(max_length=30, unique = True)
  def __str__(self):
    return "("+str(self.mid)+"):"+self.username

class Songs(models.Model):
  mid = models.CharField(unique = True)
  sid = models.AutoField(primary_key=True)
  name = models.CharField(max_length=30, unique = True)
  created = models.DateTimeField(default=timezone.now)
  dl_count = models.PositiveIntegerField(default = 0)
  last_dl = models.DateTimeField(auto_now=True)
  song_file = models.FileField(default = "jammin/media")


  class Meta:
    unique_together = (('mid','sid'),) #logically, Songs are nested under Musicians

  def __str__(self):
    return "("+str(self.mid) + "," + str(self.sid) +"):"+self.name

  def created_at(self):
    return "created at:"+str(self.created.month)+"-"+str(self.created.day)+"-"+str(self.created.year)+":"+str(self.created.hour)+":"+str(self.created.minute)+":"+str(self.created.second)

  def get_dl_count(self):
    return int(self.dl_count)


class Downloads(models.Model):
  sid = models.BigIntegerField()
  did = models.AutoField(primary_key = True)
  mid = models.BigIntegerField()
  state = models.BooleanField(default = False) # False = Not downloaded; True = Downloaded

  class Meta:
    unique_together = (('sid','did'),)         #logically, Downloads are nested under Songs, which are nested under Musicians

  def __str__(self):
    return "("+str(self.sid) + "," + str(self.did) +"):"+str(self.state)

  def downloaded_or_not(self):
    return self.state

class SongUploadForm(forms.Form):
  name = forms.CharField(label='Song Name', max_length=50)
  song_file = forms.FileField(label='Song File')
