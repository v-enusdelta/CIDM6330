from django.shortcuts import render
from rest_framework import viewsets
from .serializers import GeeksSerializer
from .models import GeeksModel

# Create your views here.

class GeeksViewSet(viewsets.ModelViewSet):
    queryset = GeeksModel.objects.all()
    serializer_class = GeeksSerializer

