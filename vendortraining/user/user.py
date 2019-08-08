from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status, viewsets
from vendortraining.models import User
from vendortraining.models.serializers import userSerializer
from vendortraining.models import Event 
from vendortraining.models.serializers import eventSerializer
from vendortraining.models import Vendor 
from vendortraining.models.serializers import vendorSerializer
from django.forms.models import model_to_dict
from rest_framework.authtoken.models import Token

class UserView(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.

    Additionally we also provide an extra `highlight` action.
    """
    queryset = User.objects.all()
    serializer_class = userSerializer.UserSerializer
    permission_classes = []
    """ @action(detail=False, methods=['post'])
    def highlight(self, request, *args, **kwargs):
        queryset = User.objects.all()
        serializer_class = userSerializer.UserSerializer(queryset)
        return Response(serializer_class.data) """
    
#user seeing ALL listed events    
    @action(detail=False, methods=['get'])
    def listAllEvents(self, request, *args, **kwargs):
        eventSet = Event.objects.all()
        serializer_class = eventSerializer.EventSerializer(eventSet, many=True)
        return Response(serializer_class.data)
    
#user seeing ONE event    
    @action(detail=False, methods=['get'])
    def listEvent(self, request, *args, **kwargs):
        eventset = Event.objects.filter(id = self.request.data.get('event_id'))
        results = eventSerializer.EventSerializer(eventset)
        return Response(results.data)
    
#user joining ONE event. dont know if we should include the change to the attendance table somehow   
    @action(detail=False, methods=['post'])
    def joinEvent(self, request, *args, **kwargs):
        queryset = Event.objects.filter(event_id = self.request.data.get('event_id'))
        serializer_class = eventSerializer.EventSerializer(queryset)
        return Response(serializer_class.data)
            
#reporting an event 
    @action(detail=False, methods=['post'])
    def reportEvent(self, request, *args, **kwargs):
        queryset = Event.objects.filter(event_id = self.request.data.get('event_id'))
        serializer_class = eventSerializer.EventSerializer(queryset)
        return Response(serializer_class.data)
    
#reporting a vendor    
    @action(detail=False, methods=['post'])
    def reportVendor(self, request, *args, **kwargs):
        queryset = Vendor.objects.filter(vendor_id = self.request.data.get('vendor_id'))
        serializer_class = vendorSerializer.VendorSerializer(queryset, many=True)
        return Response(serializer_class.data)
        
    @action(detail=False, methods=['post'])
    def profile(self, request, *args, **kwargs):
        user = User.objects.get(id = self.request.data.get('user_id'))
        user.events.all()
        token = Token.objects.get_or_create(user=user)

        try:
            res = userSerializer.UserSerializer(user)
            item = dict[res.data,token]
            return Response(item)
        except NameError:
            return Response(user, status=status.HTTP_404_NOT_FOUND)

#deleting a user profile
    @action(detail=False, methods=['get'])
    def profileDelete(self, request, *args, **kwargs):
        try:
            user = User.objects.filter(user_id = self.request.data.get('user_id')).delete()
            return Response("Successfully Deleted")
        except Exception:
            return Exception

#editing a user profile
## MAKE SURE TO USE THE RIGHT METHOD
    @action(detail=False, methods=['get'])
    def profileEdit(self, request, *args, **kwargs):
        user = User.objects.filter(id = self.request.data.get('user_id'))
        user.email = request.data.get('email')
        return Response(res.data)

#view events currently signed up for by the user
    @action(detail=False, methods=['post'])
    def userEvents(self, request, *args, **kwargs):
        queryset = Event.objects.filter(event_id = self.request.data.get('event_id'))
        serializer_class = eventSerializer.EventSerializer(queryset,many = true)
        return Response(serializer_class.data)

