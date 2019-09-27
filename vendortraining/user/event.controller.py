# TODO:
#     SET UP ROUTES IN urls.py SO THAT EACH ROUTE IN EVERY FILE (I.E. 'vendor', 'admin', 'user') IS UNIQUE.

from django.shortcuts import render
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status, viewsets
from vendortraining.models import Vendor, Event
from vendortraining.models.serializers import vendorSerializer, eventSerializer

class EventController(viewsets.ModelViewSet):
    @action(detail=False, methods=['post'])
    def viewMyEvents(self, request, *args, **kwargs):
        events = Event.objects.filter()
        serializer = eventSerializer.EventSerializer(events, many=True)
        return Response(serializer.data)
    
    #TODO COMPLETE RETURN CALL
    @action(detail=False, methods=['post'])
    def editMyEvents(self, request, *args, **kwargs):
        return() 
    
    @action(detail=False, methods=['delete'])
    def event(self, request, *args, **kwargs):
        deletedEvent = Event.objects.filter(id = self.request.data.get('id'))
        deletedEvent.delete()
        return("profile deleted")
        
    @action(detail=False, methods=['get'])
    def getAllEvents(self, request, *args, **kwargs):
        events = Event.objects.all()
        serializer = eventSerializer.EventSerializer(events, many=True)
        return Response(serializer.data)

    # reporting an event
    @action(detail=False, methods=['post'])
    def reportEvent(self, request, *args, **kwargs):
        queryset = Event.objects.filter(
            event_id=self.request.data.get('event_id'))
        serializer_class = eventSerializer.EventSerializer(queryset)
        return Response(serializer_class.data)
    # user joining ONE event. dont know if we should include the change to the attendance table somehow
    @action(detail=False, methods=['post'])
    def joinEvent(self, request, *args, **kwargs):
        queryset = Event.objects.filter(
            event_id=self.request.data.get('event_id'))
        serializer_class = eventSerializer.EventSerializer(queryset)
        return Response(serializer_class.data)