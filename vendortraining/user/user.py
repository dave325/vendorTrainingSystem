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


    """ @action(detail=False, methods=['post'])
    def highlight(self, request, *args, **kwargs):
        queryset = User.objects.all()
        serializer_class = userSerializer.UserSerializer(queryset)
        return Response(serializer_class.data) """
    
#user seeing ALL listed events    
    @action(detail=False, methods=['get'])
    def listAllEvents(self, request, *args, **kwargs):
        queryset = Event.objects.all()
        serializer_class = eventSerializer.EventSerializer(queryset)
        return Response(serializer_class.data)
    
#user seeing ONE event    
    @action(detail=False, methods=['get'])
    def listEvent(self, request, *args, **kwargs):
        return Response("Hello2")
        queryset = User.objects.all()
        serializer_class = userSerializer
    
#user joining an event. dont know how to change/update database where the attedance would change    
    @action(detail=False, methods=['post'])
    def joinEvent(self, request, *args, **kwargs):
        if 'eventid' in kwargs:
            a = Attendance(event_id = kwargs.get('eventid'), )

            queryset = User.objects.get(event_id = kwargs.get('eventid'))
            serializer_class = userSerializer
            return Response("Event Joined!")
            
#reporting an event 
    """ @action(detail=False, methods=['post'])
    def reportEvent(self, request, *args, **kwargs):
        queryset = User.objects.get(event_id = input)
        serializer_class = userSerializer
        return Response("YOU ARE IN THE DOG HOUSE") """
    
#reporting a vendor    
    """ @action(detail=False, methods=['post'])
    def reportVendor(self, request, *args, **kwargs):
        queryset = User.objects.get(event_id = input)
        serializer_class = userSerializer
        return Response("welcome to jail kind sir") """

#view user profile        
        @action(detail=False, methods=['get'])
        def profile(self, request, *args, **kwargs):
        return Response("viewing your profile")
        queryset = User.objects.all()
        serializer_class = userSerializer

#deleting a user profile
        @action(detail=False, methods=['get'])
        def profileDelete(self, request, *args, **kwargs):
        return Response("delete user profile")
        queryset = User.objects.all()
        serializer_class = userSerializer

#editing a user profile
        @action(detail=False, methods=['get'])
        def profileEdit(self, request, *args, **kwargs):
        return Response("edit user profile")
        queryset = User.objects.all()
        serializer_class = userSerializer

#view events currently signed up for 
        @action(detail=False, methods=['get'])
        def profileEvents(self, request, *args, **kwargs):
        return Response("view your events")
        queryset = User.objects.all()
        serializer_class = userSerializer