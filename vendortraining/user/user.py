from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status, viewsets
from vendortraining.models import User
from vendortraining.models.serializers import userSerializer
from vendortraining.models import Event 
from vendortraining.models.serializers import eventSerializer

class UserView(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.

    Additionally we also provide an extra `highlight` action.
    """
    @action(detail=False, methods=['post'])
    def highlight(self, request, *args, **kwargs):
        queryset = User.objects.all()
        serializer_class = userSerializer.UserSerializer(queryset)
        return Response(serializer_class.data)
    
    @action(detail=False, methods=['get'])
    def listAllEvents(self, request, *args, **kwargs):
        queryset = Event.objects.all()
        serializer_class = eventSerializer.EventSerializer(queryset)
        return Response(serializer_class.data)
    
    @action(detail=False, methods=['get'])
    def listEvent(self, request, *args, **kwargs):
        return Response("Hello2")
        queryset = User.objects.all()
        serializer_class = userSerializer
    
    @action(detail=False, methods=['post'])
    def deleteEvent(self, request, *args, **kwargs):
        return Response("Hello3")
        queryset = User.objects.all()
        serializer_class = userSerializer
