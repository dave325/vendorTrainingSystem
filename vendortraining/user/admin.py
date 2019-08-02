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
    #testing complete
    @action(detail=False, methods=['get'])
    def adminProfile(self, request, *args, **kwargs):
        #query = User.objects.get(id = self.request.data.get('id'))
        query = User.objects.filter(role__role_name  = 'admin').get(id = self.request.data.get('id'))
        serial = userSerializer.UserSerializer(query)
        return Response(serial.data)
    
    #testing complete
    @action(detail=False, methods=['post'])
    def editAdminProfile(self, request, *args, **kwargs):
        admin = User.objects.get(id = self.request.data.get('id'))
        #use this syntax for other fields
        admin.email = self.request.data.get('email')
        admin.first_name = self.request.data.get('first_name')
        admin.last_name = self.request.data.get('last_name')
        admin.phone = self.request.data.get('phone')
        admin.address = self.request.data.get('address')
        admin.password = self.request.data.get('password')
        admin.public = self.request.data.get('public')
        admin.save()

    #testing complete
    @action(detail=False, methods=['get'])
    def listCustomers(self, request, *args, **kwargs):
        query = User.objects.filter(role__role_name = "customer")
        serial = userSerializer.UserSerializer(query, many=True)
        return Response(serial.data)   
    #testing complete
    @action(detail=False, methods=['get'])
    def listVendors(self, request, *args, **kwargs):
        query = Vendor.objects.all()
        serial = vendorSerializer.VendorSerializer(query, many=True)
        return Response(serial.data)  
    #testing complete
    @action(detail=False, methods=['post'])
    def approveEvent(self, request, *args, **kwargs):
        event = Event.objects.get(event_id = self.request.data.get('event_id'))
        event.is_approved = self.request.data.get('approval')
        #check updated info
        query = Event.objects.all()
        serial = eventSerializer.EventSerializer(query, many=True)
        return Response(serial.data)

    #TODO:test
    @action(detail=False, methods=['post'])
    def deleteEvent(self, request, *args, **kwargs):
        event = Event.objects.get(event_id = self.request.data.get('event_id'))
        event.delete()
        event.save()
        #check updated info
        query = Event.objects.all()
        serial = eventSerializer.EventSerializer(query)
        return Response(serial.data)
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
        query = Event.objects.get(event_id = self.request.data.get('event_id'))
        serial = eventSerializer.EventSerializer(query)
        return Response(serial.data)

    #testing complete
    @action(detail=False, methods=['get'])
    def viewCustomer(self, request, *args, **kwargs):
        query = User.objects.filter(role__role_name  = 'customer').get(id = self.request.data.get('customer_id'))
        serial = UserSerializer.userSerializer(query)
        return Response(serial.data)
    
    #testing complete
    @action(detail=False, methods=['get'])
    def viewEvent(self, request, *args, **kwargs):
        query = Event.objects.get(event_id = self.request.data.get('event_id'))
        serial = EventSerializer.eventSerializer(query)
        return Response(serial.data)

    #testing complete
    @action(detail=False, methods=['get'])
    def viewUserInfo(self, request, *args, **kwargs):
        query = User.objects.get(id = self.request.data.get('id'))
        serial = userSerializer.UserSerializer(query)
        return Response(serial.data)

    #testing complete
    @action(detail=False, methods=['post'])
    def ApproveVendor(self, request, *args, **kwargs):
        #Vendor.objects.get(vendor_id = self.request.data.get('vendorid')).update(is_approved = self.request.data.get('approval'))
        vendor = Vendor.objects.get(vendor_id = self.request.data.get('vendor_id'))
        vendor.is_approved = self.request.data.get('approval')
        vendor.save()
        #check updated vendor
        query = Vendor.objects.get(vendor_id = self.request.data.get('vendor_id'))
        serial = vendorSerializer.VendorSerializer(query)
        return Response(serial.data)
    
    #testing complete
    @action(detail=False, methods=['post'])
    def RemoveVendor(self, request, *args, **kwargs):
        vendor = Vendor.objects.get(vendor_id = self.request.data.get('vendor_id'))
        vendor.address = ""
        vendor.phone = ""
        vendor.email =""
        vendor.save()
    
    #testing complete
    @action(detail=False, methods=['post'])
    def addVendor(self, request, *args, **kwargs):
        newVendor = Vendor(name = self.request.data.get('name'), address=self.request.data.get('address'), phone = self.request.data.get('phone'), email = self.request.data.get('email'), is_approved= False)
        newVendor.save()

