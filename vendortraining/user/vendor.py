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
    
    # TODO: I don't think this belongs here. It may belong instead in admin.
    # Return all vendors
    @action(detail=False, methods=['get'])
    def getAll(self, request, *args, **kwargs):
        s = vendorSerializer.VendorSerializer(self.queryset, many=True)
        return Response(s.data)

   
    @action(detail=False, methods=['post'])
    def editMyEvents(self, request, *args, **kwargs):
        event = Event.objects.get(id = request.data.get("event_id"))
        event.vendor_id = request.data.get("vendor_id")
        event.save()
        serial = eventSerializer.EventSerializer(event)
        return Response(serial.data) 
