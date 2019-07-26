from django.contrib import admin

# Register your models here.
rom rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status, viewsets
from vendortraining.models import User
from vendortraining.models.serializers import userSerializer
from vendortraining.models import Event
from vendortraining.models.serializers import eventSerializer
from vendortraining.models import Vendor
from vendortraining.models.serializers import vendorSerializer


class AdminView(viewset.ModelViewSet):
    @action(detail=false, method['get'])
    def profile(self, request, *args, **kwargs):
        if 'uid' in kwargs:
            queryset = User.objects.get(id = kwargs.get(uid))
            s = userSerializer.UserSerializer(queryset)
            return Response(s.data)
           
    
    @action(detail=false, method['get']) 
    def approveEvent(self, request, *args, **kwargs):
        queryset = Event.objects.all()
        s = eventSerializer.EventSerializer(queryset)
        return Response(s.data)
    
    @action(detail=false, method['get'])
    def listCustomers(self, request, *args, **kwargs):
        queryset = User.objects.all()
        s = userSerializer.UserSerializer(queryset)
        return Response(s.data)   

    @action(detail=false, method['get'])
    def listVendors(self, request, *args, **kwargs):
        queryset = Vendor.objects.all()
        s = vendorSerializer.VendorSerializer(queryset)
        return Response(s.data)  
    #approval status in event? = isApproved
    @action(detail=false, method['post'])
    def approveEvent(self, request, *args, **kwargs):
        if 'approval' in kwargs:
            queryset = Event.objects.all().update(isApproved = kwargs.get('approval'))
            e = eventSerializer.EventSerializer(queryset)
            return Response()
        