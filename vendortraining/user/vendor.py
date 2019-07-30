# TODO:
#     SET UP ROUTES IN urls.py SO THAT EACH ROUTE IN EVERY FILE (I.E. 'vendor', 'admin', 'user') IS UNIQUE.

from django.shortcuts import render
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status, viewsets
from vendortraining.models import Vendor
from vendortraining.models.serializers import vendorSerializer

class VendorView(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.

    Additionally we also provide an extra `highlight` action.
    """
    queryset = Vendor.objects.all()
    #serializer_class = userSerializer # not sure why this is needed -- Ed
    @action(detail=True, methods=['post'])
    def highlight(self, request, *args, **kwargs):
        return Response("Hello from vendor")
    
    @action(detail=False, methods=['get'])
    def getAll(self, request, *args, **kwargs):
        s = vendorSerializer.VendorSerializer(self.queryset, many=True)
        return Response(s.data)

    @action(detail=False, methods=['post'])
    def getMyProfile(self, request, *args, **kwargs):
        # qset = Vendor.objects.filter(vendor_id = self.request.data.get('vendor_id')) #self.request.data is a python dictionary. use get return the value
        # s = vendorSerializer.VendorSerializer(qset, many=True)
        # return Response(s.data)
        return()
    
    @action(detail=False, methods=['post'])
    def deleteMyProfile(self, request, *args, **kwargs):
        return()

    @action(detail=False, methods=['post'])
    def editMyProfile(self, request, *args, **kwargs):
        return()

    @action(detail=False, methods=['post'])
    def viewMyEvents(self, request, *args, **kwargs):
        return()
    
    @action(detail=False, methods=['post'])
    def editMyEvents(self, request, *args, **kwargs):
        return()
    
    @action(detail=False, methods=['post'])
    def deleteMyEvents(self, request, *args, **kwargs):
        return()

    @action(detail=False, methods=['get'])
    def listEvent(self, request, *args, **kwargs):
        eventset = Event.objects.filter(id = self.request.data.get('event_id'))
        results = eventSerializer.EventSerializer(eventset)
        return Response(results.data)
    
    @action(detail=False, methods=['post'])
    def deleteEvent(self, request, *args, **kwargs):
        eventset = Event.objects.filter(id = self.request.data.get('event_id'))
        eventSet.delete()
        return Response("Hello3")
        
