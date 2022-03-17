from django.test import TestCase
from django.contrib.auth.models import User
from .models import Resource, Meeting, MeetingMinutes, Event
import datetime
from .forms import ResourceForm, MeetingForm
from django.urls import reverse

# from django.urls import reverse
meeting = Meeting(
  title = 'MVC basics',
  date = datetime.date(2022,2,27),
  time = datetime.date(2022,2,27),
  location = '',
  agenda = ''
)
user = User(
  username = 'user1'
)
resource = Resource(
  name = "O\'Rielly\'s Fluent Python",
  type = 'book',
  date = datetime.date(2022,2,27),
  URL = '',
  userId = user,
  description = ''
)
event = Event(
  title = 'MVC meeting'
)

resourceFormData = {
  "title": "Intro to Python",
  "date": datetime.date(2022,3,2),
  "time": datetime.date(2022,3,2),
  "location": "ada's",
  "agenda": "some agenda",
}

meetingFormData = {
  "name": "Intro to Python",
  "type": "book",
  "date": datetime.date(2022,3,2),
  "URL": "https://www.notion.so/Mar-2022-bc8ad76805b849999b8fc758969fde86",
  "userId": user,
  "description": "",
}

# Create your tests here.
class MeetingTest(TestCase):
  def setUp(self):
    self.type = meeting

  def test_titlestring(self):
    self.assertEqual(str(self.type), 'MVC basics')
  
  def test_tablename(self):
    self.assertEqual(str(meeting._meta.db_table), 'meeting')

class MeetingMinutesTest(TestCase):
  def setUp(self):
    self.type = MeetingMinutes(meetingId = meeting, text = '')
  
  def test_type(self):
    self.assertTrue(self.type.meetingId)

class ResourceTest(TestCase):
  def setUp(self):
    self.type = resource
  
  def test_type(self):
    self.assertEqual(str(self.type), "O\'Rielly\'s Fluent Python")
  
  def test_namestring(self):
    self.assertIs(type(self.type.name), str)
    self.assertEqual(str(self.type.name), "O\'Rielly\'s Fluent Python")
  
  def test_tablename(self):
    self.assertEqual(str(resource._meta.db_table), 'resource')

class EventTest(TestCase):
  def setUp(self):
    self.type = event

  def test_type(self):
    self.assertEqual(str(self.type), 'MVC meeting')

  def test_tablename(self):
    self.assertEqual(str(event._meta.db_table), 'event')

class NewResourceForm(TestCase):
  # test for valid form data
  def test_resourceform(self):
    form = ResourceForm(resourceFormData)
    self.assertTrue(form.is_valid)

class NewMeetingForm(TestCase):
  # test for valid form data
  def test_meetingform(self):
    form = MeetingForm(meetingFormData)
    self.assertTrue(form.is_valid)

class New_Resource_Authentication_Test(TestCase):
  def setUp(self):
    self.test_user = User.objects.create_user(username = 'testuser1', password = 'p@ssw0rd1')

    self.resource = Resource.objects.create(name = "O\'Rielly\'s Fluent Python",
    type = 'book', date = datetime.date(2022,2,27), URL = '', userId = self.test_user, description = ''
    )
  
  def test_redirect_if_not_logged_in(self):
    response = self.client.get(reverse('newresource'))
    self.assertRedirects(response, '/accounts/login/?next=/club/newresource/')