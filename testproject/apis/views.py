from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from .serializers import GeeksSerializer
from .models import GeeksModel
from .repositories import GeeksRepository

# Create your views here.

class GeeksViewSet(viewsets.ModelViewSet):
    queryset = GeeksModel.objects.all()
    serializer_class = GeeksSerializer
    repository = GeeksRepository()
    
    def create(self, request):
        data = request.data
        response_data = self.repository.create(data)
        return Response(response_data, status=status.HTTP_201_CREATED)
    
    def list(self, request):
        response_data = self.repository.get_all()
        return Response(response_data, status=status.HTTP_200_OK)
    
    def update (self, request, pk=None):
        instance = self.get_object()
        data = request.data
        response_data = self.repository.update(instance, data)
        return Response(response_data, status=status.HTTP_200_OK)
    
    def destroy (self, request, pk=None):
        instance = self.get_object()
        self.repository.delete(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)
