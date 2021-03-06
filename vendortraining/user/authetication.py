from vendortraining import models
from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from vendortraining.models import UserInfo
from vendortraining.models import Role, Member, Vendor, Event
#from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from rest_framework import permissions, exceptions
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication, get_authorization_header
from rest_framework.authtoken.models import Token
from django.contrib.auth import get_user_model
from vendortraining.models.serializers import userSerializer, memberSerializer, vendorSerializer, eventSerializer
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

    queryset = UserInfo.objects.all()
    #authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = (permissions.AllowAny,)

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
        
        # TODO: Does msg need to be moved into the except block? or is it going to be used more globally later
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
        
        user = UserInfo.objects.get(id = user_id, role_id = role)
        if not user:
            return Response({'error': 'Invalid Credentials'}, status=HTTP_404_NOT_FOUND)
        
        new_payload = {
            #'id':user.id,
            #'email':user.email,
            #'role':user.role_id,
            #'exp': datetime.datetime.utcnow()+datetime.timedelta(minutes=60),
            'id': user['user'].get('id'),
            # TODO: check if email is working properly
            'email': user['user'].get('user').get('email'),
            'role': user['user'].get('role_id'),
            'exp': datetime.datetime.utcnow()+datetime.timedelta(minutes=60)
        }
        
        jwt_token = {'token': jwt.encode(payload, "SECRET_KEY", algorithm='HS256')}
        return Response(jwt_token, status=HTTP_200_OK)

    @action(detail=False, methods=['post'])
    def verifyToken(self, request, *args, **kwargs):
        # Split header authentication
        auth = get_authorization_header(request).split()
        if not auth:  # or auth[0].lower() != b'token'
            return HttpResponse({'Error': "Token is invalid"}, status="404")
        try:
            # Call authenticate_credentials method to validate token
            if(self.authenticate_credentials(auth[1].decode())[0]):
                return Response({'success': True, 'role_info': self.authenticate_credentials(auth[1].decode())[1]})
        except UnicodeError:
            return Response({'success': False, 'message': 'Invalid Token1'}, status="404")
    

    def get_model(self):
        return UserInfo

    '''
        Decodes the token apram and check if the user model 
        has all ofteh right information from decoded token
    '''
    def authenticate_credentials(self, token):
        msg = {'Error': "Token mismatch", 'status': "401"}
        try:
            # Decode jet token
            #TODO change "SECRET_KEY" to env variable and hide it away
            payload = jwt.decode(token, "SECRET_KEY", algorithm='HS256')
        except jwt.InvalidTokenError:
            raise exceptions.AuthenticationFailed(msg)
        # Retrieve payload information from token (May put this in a function)
        userid = payload['id']
        role = payload['role']
        try:
            # Return user from db based on decoded token
            baseUser = UserInfo.objects.get(
                id=userid
            )
            if not baseUser:
                raise exceptions.AuthenticationFailed(msg)
            if userid == baseUser.id and role == baseUser.role.id:
                return [True, baseUser.role.id]
            else:
                raise exceptions.AuthenticationFailed(
                    detail="Invalid Token", code="403")
            # have token fields to base user?
            # if not user.token['token'] == token:
            #   raise exceptions.AuthenticationFailed(msg)
        # IF jwt token has an error send exception
        except jwt.ExpiredSignature or jwt.DecodeError or jwt.InvalidTokenError:
            raise exceptions.AuthenticationFailed(
                detail="Invalid Token", code="403")
        except UserInfo.DoesNotExist:
            raise exceptions.APIException(
                default_detail="Internal server error", status_code="500")
        return False
        # return baseUser
        # return (baseUser, token)

    # def authenticate(self, request):
    @staticmethod
    def getToken(user):
        payload = {
            'id': user['user'].get('id'),
            # TODO: check and uncomment email
            #'email': user['user'].get('user').get('email'),
            'role': user['user'].get('role_id'),
            'exp': datetime.datetime.utcnow()+datetime.timedelta(minutes=60)
        }
        print(payload)
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
        # TODO: PYlint says that user_email is not being used. Remove?
        user_email = request.data.get('email')
        # authenticate user account.
        user = auth.authenticate(
            request, username=user_name, password=user_password)
        if user is not None:
            # login user account.
            auth.login(request, user)
            #authenticated_user = User.objects.get(id=user.id)
            # Get serializer object information
            serializer = userSerializer.UserSerializer(UserInfo.objects.get(id=user.id))
            userData = {}
            userData['user'] = serializer.data
            # If user is a vendor (role 2), then get all members
            if userData['user']['role_id'] == 2:
                userData.update(self.getMemberInfo(user.id))
            # Use authneticated user
            token = self.getToken(
                userData)
            obj = {
                'success': True,
                'user': userData,
                'token': token
            }

            # set cookie to transfer user name to login success page.
            return Response(obj)
        else:
            error_json = {
                'success': False,
                'error_message': 'User name or password is not correct.'}
            return Response(error_json, status="404")

    # Return all vendor,member, and events information 
    def getMemberInfo(self, id):
        data = memberSerializer.MemberSerializer(Member.objects.get(user_id=id)).data
        return {
            'vendor_info':self.getVendorInfo( data.get('vendor_id')),
            'events':self.getVendorEvents(data.get('vendor_id')),
            'members':self.getAllMembers(data.get('vendor_id'))
        }
    
    def getVendorInfo(self, id):
        return vendorSerializer.VendorSerializer(Vendor.objects.get(id=id)).data
    
    def getVendorEvents(self, id):
        return eventSerializer.EventSerializer(Event.objects.filter(vendor_id=id), many=True).data
    
    def getAllMembers(self, vendor_id):
        data = memberSerializer.MemberSerializer(Member.objects.filter(vendor_id=vendor_id), many=True).data
        return data
    

    #TODO: I don't think this comment should be here
    # view events currently signed up for by the user
    @action(detail=False, methods=['post'])
    def register(self, request, *args, **kwargs):

        user_name = request.data.get("username")
        user_password = request.data.get("password")
        user_email = request.data.get('email')
        role_id = request.data.get('role_id')
        # check if user information is not null
        if len(user_name) > 0 and len(user_password) > 0 and len(user_email) > 0:
            # check whether user account exist or not.
            user = auth.authenticate(
                request, username=user_name, password=user_password)
            # if user account do not exist.
            if user is None:
                # create user account and return the user object.
                user = get_user_model().objects.create_user(username=user_name,
                                                            password=user_password, email=user_email, 
                                                            first_name=request.data.get('firstName')
                                                            , last_name=request.data.get('lastName'))
                # update user object staff field value and save to db.
                # check if user is created before creating auth_user
                if user is not None:
                    # save user properties in auth_user table.
                    # error!: if role is not defined in the database
                    new_user = UserInfo.objects.create(id=user.id, phone=request.data.get(
                        'phone'), role_id=role_id, address=request.data.get('address'), user_id=user.id)
                    # CHeck if user is a vendor
                    if role_id == 2:
                        # Save vendor information
                        new_vendor = Vendor.objects.create(name=request.data.get('vendor_name'), address=request.data.get('vendor_address')
                        , phone=request.data.get('vendor_phone'), email=request.data.get('vendor_email'), is_approved=False)
                        new_vendor.save()
                        # Use current user and create user
                        new_member = Member.objects.create(company_role='creator', user_id=user.id, vendor_id=new_vendor.id)
                        new_member.save()
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
