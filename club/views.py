from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import login_required 
from django.urls import reverse_lazy

from club.forms import MeetingForm, ResourceForm
from .models import Resource, Meeting

# Create your views here.
def index(request):
  return render(request, 'club/index.html')

def resources(request):
  resource_list = Resource.objects.all()
  return render(request, 'club/resources.html', {'resource_list': resource_list})

def meetings(request):
  meetings = Meeting.objects.all()
  return render(request, 'club/meetings.html', {'meetings' : meetings})

def meetingDetail(request, id):
  meeting = get_object_or_404(Meeting, pk=id)
  return render(request, 'club/meetingdetail.html', {'meeting' : meeting})

@login_required
def resourceForm(request):
  form = ResourceForm
  if request.method == 'POST':
    form = ResourceForm(request.POST)
    if form.is_valid():
      post = form.save(commit = True)
      post.save()
      form = ResourceForm()
  else:
    form = ResourceForm()
  return render(request, 'club/newresource.html', {'form' : form})

def meetingForm(request):
  form = MeetingForm
  if request.method == 'POST':
    form = MeetingForm(request.POST)
    if form.is_valid():
      post = form.save(commit = True)
      post.save()
      form = MeetingForm()
  else:
    form = MeetingForm()
  return render(request, 'club/meetingform.html', {'form' : form})

def loginmessage(request):
  return render(request, 'club/loginmessage.html')

def logoutmessage(request):
  return render(request, 'club/logoutmessage.html')