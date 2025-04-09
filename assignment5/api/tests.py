from django.test import TestCase
from rest_framework.test import APIClient
from unittest.mock import patch
from django.utils import timezone
from datetime import timedelta
from .models import User, Session, Event

# Create your tests here.
class EventTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create(
            userid=1,
            username= 'testuser',
            password= 'testpassword',
            email='test@test.com',
            isadmin=False,
            isreporter=False,
            isanalyst=False,
            isviewer=True)
        self.session = Session.objects.create(
            userid=self.user, 
            sessionid=123, 
            sessionkey='session_key_123',
            created_at=timezone.now(),
            expires_at=timezone.now() + timedelta(hours=1)
        )

    def test_event_viewset_create(self):
        payload = {
            'eventid': 1,
            'sessionid': self.session.sessionid,
            'itemid': 'item123',
            'eventtime': timezone.now(),
            'eventtype': 'modify'
        }

        response = self.client.post('/api/events/', payload, format='json')
        self.assertEqual(response.status_code, 404)
        self.assertEqual(Event.objects.count(), 1)
        self.assertEqual(Event.objects.get().itemid, 'item123')

    @patch('assignment5.api.tasks.create_event_task.delay')
    def test_event_create_view_async(self, mock_create_event_task):
        payload = {
            'sessionid': self.session.sessionid,
            'itemid': 'item123',
            'eventtype': 'modify'
        }

        response = self.client.post('/api/events/create/async/', payload, format='json')
        self.assertEqual(response.status_code, 404)
        mock_create_event_task.assert_called_once_with(self.session.sessionid, 'item123', 'modify')