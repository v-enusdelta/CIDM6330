from rest_framework import serializers
from .models import GeeksModel

class GeeksSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = GeeksModel
        fields = ('title', 'description')
