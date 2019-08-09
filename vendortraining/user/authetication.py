from vendortraining import models
from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from vendortraining.models import user
from vendortraining.models.serializers import userSerializer
from vendortraining.models import Role
from vendortraining.models.serializers import roleSerializer

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from rest_framework import permissions, exceptions
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication, get_authorization_header
from rest_framework.authtoken.models import Token

import jwt
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK
)

#jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
#jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

class UserAuthetication(viewsets.ModelViewSet):
    
    queryset = User.objects.all()
    #authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = (permissions.AllowAny,)
    #todo: with login cred, check db
    @action(detail=False, methods=['post'])
    def checkUser(self, request, *args, **kwargs):
        baseUser = user.User.objects.get(id = self.request.data.get('user_id'))
        res = userSerializer.UserSerializer(baseUser)
        if self.request.data.get('user_id') == 5:
            return res.data
        else:
            return False  
    @action(detail=False, methods=['post'])
    def checkId(self, request, *args, **kwargs):
        if user.User.objects.filter(id == self.request.data.get('user_id')):
            return True
        else:
            return False
    #Todo: verify token key and check with db. refresh if correct
    @action(detail=False, methods=['get'])
    def viewAuthUser(self, request, *args, **kwargs):
        auth = get_authorization_header(request).split()
        if not auth: #or auth[0].lower() != b'token'
            return Response(auth)

        try:
            token = auth[1].decode()
        except UnicodeError:                                               
            msg = _('Invalid token header. Token string should not contain invalid  characters.')
            raise exceptions.AuthenticationFailed(msg)
        
        baseUser = self.authenticate_credentials(token)
        #serial = userSerializer.UserSerializer(baseUser)
        return Response(baseUser)
    
    def authenticate_header(self, request):
        return 'Token'

    def get_model(self):
        return User

    def authenticate_credentials(self, token):
        model = self.get_model()
        msg = {'Error': "Token mismatch",'status' :"401"}
        try:
            payload = jwt.decode(token, "SECRET_KEY", algorithm='HS256')
        except jwt.InvalidTokenError:
            raise exceptions.AuthenticationFailed(msg)
        email = payload['email']
        userid = payload['id']
        role = payload['role']
        try:
            baseUser = user.User.objects.get(
                #email=email,
                id=userid
                #is_active=True
            )

            if not baseUser:
                raise exceptions.AuthenticationFailed(msg)
            #have token fields to base user?
            #if not user.token['token'] == token:
            #   raise exceptions.AuthenticationFailed(msg)
        
               
        except jwt.ExpiredSignature or jwt.DecodeError or jwt.InvalidTokenError:
            return HttpResponse({'Error': "Token is invalid"}, status="403")
        except User.DoesNotExist:
            return HttpResponse({'Error': "Internal server error"}, status="500")
        
        role_query = Role.objects.get(id = role)
        serial = roleSerializer.RoleSerializer(role_query)
        return serial.data['role_name']
        #return baseUser
        #return (baseUser, token)
    
    #def authenticate(self, request):
        

