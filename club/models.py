from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Meeting(models.Model):
  title = models.CharField(max_length=255)
  date = models.DateTimeField()
  time = models.DateTimeField()
  location = models.TextField(null=True, blank=True)
  agenda = models.TextField(null=True, blank=True)

  def __str__(self):
    return self.title

  class Meta:
    db_table='meeting'

class MeetingMinutes(models.Model):
  meetingId = models.ForeignKey(Meeting, on_delete = models.DO_NOTHING)
  attendance = models.ManyToManyField(User)
  text = models.TextField(null=True, blank=True)

  def __str__(self):
    return self.text
  
  class Meta:
    db_table='minute'

class Resource(models.Model):
  name = models.CharField(max_length=255)
  type = models.CharField(max_length=255)
  date = models.DateField()
  URL = models.URLField()
  userId = models.ForeignKey(User, on_delete = models.CASCADE)
  description = models.TextField(null=True, blank=True)

  def __str__(self):
    return self.name

  class Meta:
    db_table='resource'

class Event(models.Model):
  title = models.CharField(max_length=255)
  location = models.TextField()
  date = models.DateField()
  time = models.DateTimeField()
  description = models.TextField()
  userId = models.ManyToManyField(User)
  
  def __str__(self):
    return self.title
  
  class Meta:
    db_table='event'