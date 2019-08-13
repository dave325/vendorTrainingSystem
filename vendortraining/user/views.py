from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status, viewsets
from vendortraining.models import User
from vendortraining.models.serializers import userSerializer
from vendortraining.user import authetication

import jwt, json, datetime

from django.contrib.auth import authenticate, login
from rest_framework import permissions 
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication, get_authorization_header
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
    #ToDO: input: user_id, output: token with role_id, email, and id
    @action(detail=False, methods=['get'])
    def getToken(self, request, *args, **kwargs):
        
       # token, _ = Token.objects.get_or_create(user=superUser)
        #super user check
        #super_username = request.data.get("super_username")
        #super_password = request.data.get("super_password")
        #if super_username is None or super_password is None:
        #    return Response({'error': 'Please provide both username and password'},
        #                status=HTTP_400_BAD_REQUEST)
        #superUser = authenticate(username=super_username, password=super_password)
        #if not superUser:
        #    return Response({'error': 'Invalid Credentials'},
        #                status=HTTP_404_NOT_FOUND)
        #token, _ = Token.objects.get_or_create(user=superUser)

        user = User.objects.get(id = self.request.data.get('user_id'))

        if user is None:
            return Response('user not found', status=HTTP_404_NOT_FOUND)
        
        #role_id, email, id ...
        payload = {
            'id':user.id,
            'email':user.email,
            'role':user.role_id,
            'exp': datetime.datetime.utcnow()+datetime.timedelta(minutes=60)
        }

        jwt_token = {'token': jwt.encode(payload, "SECRET_KEY", algorithm='HS256')}
        #jwt_token.update({'superToken':token.key})
        
        return Response(jwt_token, status=HTTP_200_OK)
        #return Response({'token': jwt_token.get('token')}, status=HTTP_200_OK)
    @action(detail=False, methods=['get'])
    def refreshToken(self, request, *args, **kwargs):
        auth = get_authorization_header(request).split()
        if not auth: #or auth[0].lower() != b'token'
            return Response(auth)

        try:
            token = auth[1].decode()
        except UnicodeError:                                               
            msg = _('Invalid token header. Token string should not contain invalid  characters.')
            raise exceptions.AuthenticationFailed(msg)
        
        msg = {'Error': "Token mismatch",'status' :"401"}
        try:
            payload = jwt.decode(token, "SECRET_KEY", algorithm='HS256')
        except jwt.InvalidTokenError:
            raise exceptions.AuthenticationFailed(msg)

        user_id = payload['id']
        email = payload['email']
        role = payload['role']
        exp = payload['exp']
        
        if not user_id or not email or not role or not exp:
            return Response({'error': 'Invalid Token'}, status=HTTP_400_BAD_REQUEST)
        
        user = User.objects.get(id = user_id, email = email, role_id = role)
        if not user:
            return Response({'error': 'Invalid Credentials'}, status=HTTP_404_NOT_FOUND)
        
        new_payload = {
            'id':user.id,
            'email':user.email,
            'role':user.role_id,
            'exp': datetime.datetime.utcnow()+datetime.timedelta(minutes=60)
        }
        
        jwt_token = {'token': jwt.encode(payload, "SECRET_KEY", algorithm='HS256')}
        return Response(jwt_token, status=HTTP_200_OK)


           

        
    
#def jwt_response_payload_handler(token, user=None, request=None):
#    return {
#        'token': token,
#        'user': UserSerializer(user, context={'request':request}).data
#    }
    
        
