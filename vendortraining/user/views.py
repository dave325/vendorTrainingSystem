from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status, viewsets
from vendortraining.models import User
from vendortraining.models.serializers import userSerializer
from vendortraining.user import authetication

import jwt, json

from django.contrib.auth import authenticate, login
from rest_framework import permissions 
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.authtoken.models import Token

from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK
)

class UserView(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.

    Additionally we also provide an extra `highlight` action.
    """
    queryset = User.objects.all() # imports the user object from vendortraining.models
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

    @action(detail=False, methods=['get'])
    def getToken(self, request, *args, **kwargs):
        super_username = request.data.get("super_username")
        super_password = request.data.get("super_password")
        user_password = request.data.get("user_password")
        user = User.objects.get(id = self.request.data.get('user_id'))

        if super_username is None or super_password is None:
            return Response({'error': 'Please provide both username and password'},
                        status=HTTP_400_BAD_REQUEST)
        superUser = authenticate(username=super_username, password=super_password)
        if not superUser:
            return Response({'error': 'Invalid Credentials'},
                        status=HTTP_404_NOT_FOUND)
        token, _ = Token.objects.get_or_create(user=superUser)


        if user is None:
            return Response('user not found')
        
        if user_password != user.password:
            return Response('invalid credentials')
        payload = {
            'id':user.id,
            'password':user.password
        }

        jwt_token = {'token': jwt.encode(payload, "SECRET_KEY", algorithm='HS256')}
        jwt_token.update({'superToken':token.key})
        return Response(jwt_token)
        #return Response({'token': jwt_token.get('token')}, status=HTTP_200_OK)
    
#def jwt_response_payload_handler(token, user=None, request=None):
#    return {
#        'token': token,
#        'user': UserSerializer(user, context={'request':request}).data
#    }
    
        
