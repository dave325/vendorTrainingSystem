# TODO:
#     SET UP ROUTES IN urls.py SO THAT EACH ROUTE IN EVERY FILE (I.E. 'vendor', 'admin', 'user') IS UNIQUE.

from django.shortcuts import render
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status, viewsets
from vendortraining.models import Vendor, Event
from vendortraining.models.serializers import vendorSerializer, eventSerializer

class VendorView(viewsets.ModelViewSet):
    
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.

    Additionally we also provide an extra `highlight` action.
    """
    queryset = Vendor.objects.all()
    permission_classes = []
    #serializer_class = userSerializer # not sure why this is needed -- Ed
    
    # Return all vendors
    @action(detail=False, methods=['get'])
    def getAll(self, request, *args, **kwargs):
        s = vendorSerializer.VendorSerializer(self.queryset, many=True)
        return Response(s.data)

    #Peter: should use post methods unless other guys are okay with delete methods
    @action(detail=False, methods=['delete'])
    def deleteMyProfile(self, request, *args, **kwargs):
        vendorProfile = Vendor.objects.filter(vendor_id = self.request.data.get('vendor_id'))
        vendorProfile.delete()
        return("profile deleted")

    #TODO Peter: it shows no error message when invalid input is given 
    @action(detail=False, methods=['post'])
    def editMyProfile(self, request, *args, **kwargs):
        vendorProfile = Vendor.objects.filter(vendor_id = self.request.data.get('vendor_id'))
        y = ""
        d = {}
        for x in self.request.data:
            if len(str(self.request.data.get(x))) == 0: #If the data field is empty, we assume that we do not want to update that value----How it works:We convert to str to use len(). Probably a more elegent way of doing this though
                continue
            d[x] = self.request.data.get(x)
            # x = str(self.request.data.get(x))
            # y = y + " " + x

        vendorProfile.update(**d)

        return Response(y) # for debug-- not nessicary

    
    @action(detail=False, methods=['post'])
    def editMyEvents(self, request, *args, **kwargs):
        event = Event.objects.get(id = request.data.get("event_id"))
        event.vendor_id = request.data.get("vendor_id")
        event.save()
        serial = eventSerializer.EventSerializer(event)
        return Response(serial.data) 
    
    '''
        delete event based on id
    '''
    @action(detail=False, methods=['delete'])
    def event(self, request, *args, **kwargs):
        deletedEvent = Event.objects.filter(id = self.request.data.get('id'))
        deletedEvent.delete()
        return("profile deleted")