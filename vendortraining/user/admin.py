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
from vendortraining.models import Role



class AdminView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    #TODO: check if the user is admin
    @action(detail=False, methods=['get'])
    def adminProfile(self, request, *args, **kwargs):
        query = User.objects.get(id = self.request.data.get('id'))
        serial = userSerializer.UserSerializer(query)
        return Response(serial.data)
         
    #TODO: make sure users are customers, test output
    @action(detail=False, methods=['get'])
    def listCustomers(self, request, *args, **kwargs):
        query = User.objects.filter(role_id__role_name = 'customer')
        serial = userSerializer.UserSerializer(query, many=True)
        return Response(serial.data)   
    #TODO: make sure users are vendors
    @action(detail=False, methods=['get'])
    def listVendors(self, request, *args, **kwargs):
        query = Vendor.objects.all()
        serial = vendorSerializer.VendorSerializer(query, many=True)
        return Response(serial.data)  
    #approval status in event? = isApproved
    @action(detail=False, methods=['post'])
    def approveEvent(self, request, *args, **kwargs):
        if self.request.data['approval'] and self.request.data['eventid']:
            Event.objects.get(event_id = self.request.data.get('eventid')).update(is_approved = self.request.data.get('approval'))
            #check updated info
            query = Event.objects.all()
            serial = eventSerializer.EventSerializer(query, many=True)
            return Response(serial.data)
        else:
            return Response('invalid input type')

    @action(detail=False, methods=['post'])
    def deleteEvent(self, request, *args, **kwargs):
        if self.request.data['eventid']:
            Event.objects.get(event_id = self.request.data.get('eventid')).delete()
            #check updated info
            query = Event.objects.all()
            serial = eventSerializer.EventSerializer(query)
            return Response(serial.data)
        else:
            return Response('invalid input type')
    #TODO: change fields to values in input
    @action(detail=False, methods=['post'])
    def editEvent(self, request, *args, **kwargs):
        eventEdit = Event.objects.filter(event_id = self.request.data.get('event_id'))
        d = {}
        for x in self.request.data:
            if len(str(self.request.data.get(x))) == 0:
                continue
            d[x] = self.request.data.get(x)

        vendorProfile.update(**d)
        return Response(d)

    @action(detail=False, methods=['get'])
    def listEvent(self, request, *args, **kwargs):
        if self.request.data['eventid']:
            query = Event.objects.get(event_id = self.request.data.get('eventid'))
            serial = eventSerializer.EventSerializer(query)
            return Response(serial.data)
        else:
            return Response('invalid input type')

    @action(detail=False, methods=['get'])
    def viewCustomer(self, request, *args, **kwargs):
        if self.request.data['customerid']:
            query = User.objects.filter(role_id__role_name = 'customer').get(id = self.request.data.get('customerid'))
            serial = UserSerializer.userSerializer(query)
            return Response(serial.data)
        else:
            return Response("invalid input type")
    
    @action(detail=False, methods=['get'])
    def viewEvent(self, request, *args, **kwargs):
        if self.request.data['eventid']:
            query = Event.objects.get(event_id = self.request.data.get('eventid'))
            serial = EventSerializer.eventSerializer(query)
            return Response(serial.data)
        else:
            return Response('invalid input type')

    @action(detail=False, methods=['get'])
    def viewUserInfo(self, request, *args, **kwargs):
        if self.request.data['uid']:
            query = User.objects.get(id = self.request.data.get('uid'))
            serial = userSerializer.UserSerializer(query)
            return Response(serial.data)
        else:
            return Response('invalid input')

    @action(detail=False, methods=['post'])
    def ApproveVendor(self, request, *args, **kwargs):
        if self.request.data.get('approval') and self.request.data.get('vendorid'):
            Vendor.objects.get(vendor_id = vendorid).update(is_approved = self.request.data.get('approval'))

        else:
            return Response('invalid input')
    
    @action(detail=False, methods=['post'])
    def RemoveVendor(self, request, *args, **kwargs):
        if self.request.data.get('vendorid'):
            Vendor.objects.get(vendor_id = vendorid).update(address = '')
            Vendor.objects.get(vendor_id = vendorid).update(phone = '')
            Vendor.objects.get(vendor_id = vendorid).update(email = '')
            #reduce database call
        else:
            return Response('invalid input')
    

    @action(detail=False, methods=['post'])
    def addVendor(self, request, *args, **kwargs):
        newVendor = Vendor(name = self.request.data.get('name'), address=self.request.data.get('address'), phone = self.request.data.get('phone'), email = self.request.data.get('email'))
        newVendor.save()

