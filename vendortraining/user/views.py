from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status, viewsets
from vendortraining.models import UserInfo
from vendortraining.models.serializers import userSerializer
from vendortraining.user import authetication

import jwt, json, datetime

from django.contrib.auth import authenticate, login
from rest_framework import permissions 
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication, get_authorization_header
from rest_framework.authtoken.models import Token



class UserView(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.

    Additionally we also provide an extra `highlight` action.
    """
    queryset = UserInfo.objects.all() # imports the user object from vendortraining.models
    permission_classes = (permissions.AllowAny,)
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
    #ToDO: input: user_id, output: token with role_id, email, and id
    #@action(detail=False, methods=['get'])
    



           

        
    
#def jwt_response_payload_handler(token, user=None, request=None):
#    return {
#        'token': token,
#        'user': UserSerializer(user, context={'request':request}).data
#    }
    
        
