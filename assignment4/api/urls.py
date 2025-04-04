from django.urls import path, include
from rest_framework import routers
from .views import UserViewSet, SessionViewSet, EventViewSet

router = routers.DefaultRouter()

router.register(r'users', UserViewSet)
router.register(r'sessions', SessionViewSet)
router.register(r'events', EventViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('', include('rest_framework.urls'))
]