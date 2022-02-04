from django.db import models
from django.contrib.auth.models import User

#####################################
#####################################

# Meeting which will have fields for meeting title, meeting date, meeting time, location, Agenda

# Meeting Minutes which will have fields for meeting id (a foreign key), attendance (a many to many field with User), Minutes text

# Resource which will have fields for resource name, resource type, URL, date entered, user id (foreign key with User), and description

# Event which will have fields for event title, location, date, time, description and the user id of the member that posted it

#####################################
#####################################

# register the models in admin.py

# Create and troubleshoot the models, and then make migrations and migrate

# Create a superuser and open the admin site

# Upload the code to GitHub and post the url in canvas

#####################################
#####################################

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