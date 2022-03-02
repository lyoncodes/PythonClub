from django.shortcuts import get_object_or_404, render

from club.forms import MeetingForm, ResourceForm
from .models import Resource, Meeting
from django.urls import reverse_lazy

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
  return render(request, 'club/resourceform.html', {'form' : form})

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