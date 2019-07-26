from django.contrib import admin

# Register your models here.
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status, viewsets
from vendortraining.models import User
from vendortraining.models.serializers import userSerializer
from vendortraining.models import Event
from vendortraining.models.serializers import eventSerializer
from vendortraining.models import Vendor
from vendortraining.models.serializers import vendorSerializer


class AdminView(viewset.ModelViewSet):
    #TODO: check if can be imported from other classes
    @action(detail=False, methods=['get'])
    def profile(self, request, *args, **kwargs):
        if self.request.data['uid']:
            queryset = User.objects.get(id = self.request.data['uid'])
            s = userSerializer.UserSerializer(queryset)
            return Response(s.data)
           
    #TODO: make sure users are customers, test output
    @action(detail=False, methods=['get'])
    def listCustomers(self, request, *args, **kwargs):
        queryset = User.objects.filter(Role.objects.filter(role_name = "customer").role_id = role_id)
        s = userSerializer.UserSerializer(queryset)
        return Response(s.data)   
    #TODO: make sure users are vendors
    @action(detail=False, methods=['get'])
    def listVendors(self, request, *args, **kwargs):
        queryset = Vendor.objects.all()
        s = vendorSerializer.VendorSerializer(queryset)
        return Response(s.data)  
    #approval status in event? = isApproved
    @action(detail=False, methods=['post'])
    def approveEvent(self, request, *args, **kwargs):
        if self.request.data['approval'] and self.request.data['eventid']:
            Event.objects.get(event_id = self.request.data['eventid']).update(isApproved = self.request.data['approval'])
            queryset = Event.objects.all()
            s = eventSerializer.EventSerializer(queryset)
            return Response(s.data)
        else:
            return Response('invalid input type')

    @action(detail=False, methods=['post'])
    def deleteEvent(self, request, *args, **kwargs):
        if self.request.data['eventid']:
            Event.objects.get(event_id = self.request.data['eventid']).delete()
            queryset = Event.objects.all()
            s = eventSerializer.EventSerializer(queryset)
            return Response(s.data)
        else:
            return Response('invalid input type')
    #TODO: change fields to values in input
    @action(detail=False, methods=['post'])
    def editEvent(self, request, *args, **kwargs):
        if self.request.data['eventid']:
            Event.objects.get(event_id = self.request.data['eventid']).update()
        else:
            return Response('invalid input type')

    @action(detail=False, methods=['get'])
    def listEvent(self, request, *args, **kwargs):
        if self.request.data['eventid']:
            queryset = Event.objects.get(event_id = self.request.data['eventid'])
            s = eventSerializer.EventSerializer(queryset)
            return Response(s.data)
        else:
            return Response('invalid input type')
        


