from django.urls import path

from . import views

urlpatterns = [
  path('', views.index, name='index'),
  path('resources/', views.resources, name='resources'),
  path('meetings/', views.meetings, name='meetings'),
  path('meeting/<int:id>/', views.meetingDetail, name="meeting"),
  path('newresource/', views.resourceForm, name="newresource"),
  path('newmeeting/', views.meetingForm, name="meetingform"),
  path('loginmessage/', views.loginmessage, name="loginmessage"),
  path('logoutmessage/', views.logoutmessage, name="logoutmessage")
]