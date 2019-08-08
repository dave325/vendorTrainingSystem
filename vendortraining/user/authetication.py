from vendortraining import models
from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from vendortraining.models.serializers import userSerializer

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from rest_framework import permissions 
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.authtoken.models import Token

from django.views.decorators.csrf import csrf_exempt
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
    permission_classes = (permissions.IsAuthenticated,)
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
    @action(detail=False, methods=['post'])
    def viewAuthUser(self, request, *args, **kwargs):
        username = request.data.get("username")
        password = request.data.get("password")
        if username is None or password is None:
            return Response({'error': 'Please provide both username and password'},
                        status=HTTP_400_BAD_REQUEST)
        user = authenticate(username=username, password=password)
        if not user:
            return Response({'error': 'Invalid Credentials'},
                        status=HTTP_404_NOT_FOUND)
        token, _ = Token.objects.get_or_create(user=user)
        return Response({'token': token.key},
                    status=HTTP_200_OK)

    