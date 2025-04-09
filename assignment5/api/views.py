from django.shortcuts import render
from rest_framework import viewsets, status
from .serializers import UserSerializer, SessionSerializer, EventSerializer
from .models import User, Session, Event
from rest_framework.response import Response
from rest_framework.views import APIView
from .tasks import create_event_task

# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class SessionViewSet(viewsets.ModelViewSet):
    queryset = Session.objects.all()
    serializer_class = SessionSerializer

class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data)

class EventCreateView(APIView):
    def post(self, request):
        try:
            session_id = request.data.get('session_id')
            item_id = request.data.get('item_id')
            event_type = request.data.get('event_type')
            
             # Call the Celery task to create an event asynchronously
            create_event_task.delay(session_id, item_id, event_type)
            return Response({"status": "Event creation task has been queued."}, status=status.HTTP_202_ACCEPTED)
        except Exception as e:
            # If the data is not valid, return an error response
            return Response({"status": "Invalid data"}, status=status.HTTP_400_BAD_REQUEST)