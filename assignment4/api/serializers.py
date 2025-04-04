from rest_framework import serializers
from .models import User, Session, Event

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['userid', 'username', 'password', 'email', 'isadmin', 'isreporter', 'isanalist', 'isviewer']
        extra_kwargs = {'password': {'write_only': True}}

class SessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Session
        fields = ['sessionid', 'userid', 'sessionkey', 'created_at', 'expires_at']

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ['eventid', 'sessionid', 'itemid', 'eventtime', 'eventtype']