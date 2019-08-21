from vendortraining import models
from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from vendortraining.models import User
from vendortraining.models.serializers import userSerializer
from vendortraining.models import Role
from vendortraining.models.serializers import roleSerializer

#from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from rest_framework import permissions, exceptions
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication, get_authorization_header
from rest_framework.authtoken.models import Token
from django.contrib import auth

import jwt
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK
)
import datetime

#jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
#jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER


class UserAuthetication(viewsets.ModelViewSet):

    queryset = User.objects.all()
    #authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = (permissions.AllowAny,)

    @action(detail=False, methods=['post'])
    def verifyToken(self, request, *args, **kwargs):
        auth = get_authorization_header(request).split()
        if not auth:  # or auth[0].lower() != b'token'
            return HttpResponse({'Error': "Token is invalid"}, status="404")
        try:
            #if(self.authenticate_credentials(auth[1].decode())):
            return Response({'success': True, 'info':self.authenticate_credentials(auth[1].decode())})
        except UnicodeError:
            return Response({'success': False, 'message': 'Invalid Token'}, status="404")
    # todo: with login cred, check db
    @action(detail=False, methods=['post'])
    def checkUser(self, request, *args, **kwargs):
        baseUser = user.User.objects.get(id=self.request.data.get('user_id'))
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
    # Todo: verify token key and check with db. refresh if correct
    @action(detail=False, methods=['get'])
    def viewAuthUser(self, request, *args, **kwargs):
        auth = get_authorization_header(request).split()
        if not auth:  # or auth[0].lower() != b'token'
            return Response(auth)

        try:
            token = auth[1].decode()
        except UnicodeError:
            msg = _(
                'Invalid token header. Token string should not contain invalid  characters.')
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
        msg = {'Error': "Token mismatch", 'status': "401"}
        try:
            payload = jwt.decode(token, "SECRET_KEY", algorithm='HS256')
        except jwt.InvalidTokenError:
            raise exceptions.AuthenticationFailed(msg)
        email = payload['email']
        userid = payload['id']
        role = payload['role']
        try:
            baseUser = User.objects.get(
                # email=email,
                id=userid
                # is_active=True
            )

            if not baseUser:
                raise exceptions.AuthenticationFailed(msg)
            if email == baseUser.email and userid == baseUser.id and role == baseUser.role.id:
                return True
            else:
                raise exceptions.AuthenticationFailed(detail="Invalid Token", code="403")
            # have token fields to base user?
            # if not user.token['token'] == token:
            #   raise exceptions.AuthenticationFailed(msg)

        except jwt.ExpiredSignature or jwt.DecodeError or jwt.InvalidTokenError:
            raise exceptions.AuthenticationFailed(detail="Invalid Token", code="403")
        except User.DoesNotExist:
            raise exceptions.APIException(default_detail="Internal server error", status_code="500")
        return False
        # return baseUser
        # return (baseUser, token)

    # def authenticate(self, request):
    @staticmethod
    def getToken(user):
        payload = {
            'id': user.id,
            'email': user.email,
            'role': user.role_id,
            'exp': datetime.datetime.utcnow()+datetime.timedelta(minutes=60)
        }

        jwt_token = {'token': jwt.encode(
            payload, "SECRET_KEY", algorithm='HS256')}
        # jwt_token.update({'superToken':token.key})

        return jwt_token
        # return Response({'token': jwt_token.get('token')}, status=HTTP_200_OK)
    # view events currently signed up for by the user
    @action(detail=False, methods=['post'])
    # @csrf_exempt
    def login(self, request, *args, **kwargs):
        user_name = request.data.get("username")
        user_password = request.data.get("password")
        user_email = request.data.get('email')
        # authenticate user account.
        user = auth.authenticate(
            request, username=user_name, password=user_password)
        if user is not None:
            # login user account.
            
            auth.login(request, user)
            authenticated_user = User.objects.get(id=user.id)
            serializer = userSerializer.UserSerializer(authenticated_user)
            # Use authneticated user
            token = self.getToken(
                authenticated_user)
            
            obj = {
                # 'user': user,
                'success':True,
                'user': serializer.data,
                'token': token
            }

            # set cookie to transfer user name to login success page.
            return Response(obj)
        else:
            error_json = {
                'success' : False,
                'error_message': 'User name or password is not correct.'}
            return HttpResponse(error_json, status="404")

    # view events currently signed up for by the user
    @action(detail=False, methods=['post'])
    def register(self, request, *args, **kwargs):

        user_name = request.data.get("username")
        user_password = request.data.get("password")
        user_email = request.data.get('email')
        if len(user_name) > 0 and len(user_password) > 0 and len(user_email) > 0:
            # check whether user account exist or not.
            user = auth.authenticate(
                request, username=user_name, password=user_password)
            # if user account do not exist.
            if user is None:
                # create user account and return the user object.
                user = get_user_model().objects.create_user(username=user_name,
                                                            password=user_password, email=user_email)
                # update user object staff field value and save to db.
                # check if user is created before creating auth_user
                if user is not None:
                    # save user properties in sqlite auth_user table.
                    new_user = User.objects.create(id=user.id, phone=request.data.get(
                        'phone'), role_id=1, email=user_email, address=request.data.get('address'))
                    new_user.save()
                    user.save()
                # redirect web page to register success page.
                return Response("Done")
            else:
                error_json = {
                    'error_message': 'User account exist, please register another one.'}
                return Response(error_json)
        else:
            error_json = {
                'error_message': 'User name, password and email can not be empty.'}
            return Response(error_json)
