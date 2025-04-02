from .models import GeeksModel
from .serializers import GeeksSerializer

class GeeksRepository:
    def create(self, data):
        seralizer = GeeksSerializer(data=data)
        if seralizer.is_valid():
            return seralizer.data
        else:
            return seralizer.errors
        
    def get_all(self):
        data = GeeksModel.objects.all()
        seralizer = GeeksSerializer(data, many=True)
        return seralizer.data

    def update(self, instance, data):
        serializer = GeeksSerializer(instance, data=data)
        if serializer.is_valid():
            serializer.save()
            return serializer.data
        else:
            return serializer.errors

    def delete(self, instance):
        instance.delete()