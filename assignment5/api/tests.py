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
            username='testuser', 
            email='test@test.com', 
            password='testpassword')
        self.session = Session.objects.create(
            user=self.user, 
            sessionid='session123', 
            sessionkey='session_key_123',
            created_at=timezone.now(),
            expires_at=timezone.now() + timedelta(hours=1)
        )

    def test_event_viewset_create(self):
        payload = {
            'sessionid': self.session.sessionid,
            'itemid': 'item123',
            'eventtype': 'modify'
        }

        response = self.client.post('/api/events/', payload, format='json')
        self.assertEqual(response.status_code, 201)
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
        self.assertEqual(response.status_code, 202)
        mock_create_event_task.assert_called_once_with(self.session.sessionid, 'item123', 'modify')