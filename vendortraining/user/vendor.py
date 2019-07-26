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
    #serializer_class = userSerializer # not sure why this is needed -- Ed
    @action(detail=False, methods=['post'])
    def highlight(self, request, *args, **kwargs):
        return Response("Hello from vendor")
    
    @action(detail=False, methods=['post'])
    def getAll(self, request, *args, **kwargs):
        queryset = Vendor.objects.all()
        s = vendorSerializer.VendorSerializer(queryset, many=True)
        return Response(s.data)

    @action(detail=False, methods=['post'])
    def getProfile(self, request, *args, **kwargs):
        queryset = Vendor(vendor_id = 1)
        s = vendorSerializer.VendorSerializer(self.queryset, many=True)
        return Response(s.data)
    
    @action(detail=False, methods=['get'])
    def listEvent(self, request, *args, **kwargs):
        return Response("Hello2")
    
    @action(detail=False, methods=['post'])
    def deleteEvent(self, request, *args, **kwargs):
        return Response("Hello3")
        
