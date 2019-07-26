from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status, viewsets
from vendortraining.models import User
from vendortraining.models.serializers import userSerializer

class UserView(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.

    Additionally we also provide an extra `highlight` action.
    """
    queryset = User.objects.all()
    #serializer_class = userSerializer
    @action(detail=False, methods=['post'])
    def highlight(self, request, *args, **kwargs):
        s = userSerializer.UserSerializer(self.queryset, many=True)
        return Response(s.data)
    
    @action(detail=False, methods=['get'])
    def listAllEvents(self, request, *args, **kwargs):
        return Response("Hello1")
    
    @action(detail=False, methods=['get'])
    def listEvent(self, request, *args, **kwargs):
        return Response("Hello2")
    
    @action(detail=False, methods=['post'])
    def deleteEvent(self, request, *args, **kwargs):
        return Response("Hello3")
        
