from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
# Create your views here.
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status, viewsets
from vendortraining.models import UserInfo
from vendortraining.models import Event
from vendortraining.models.serializers import eventSerializer
from vendortraining.models import Vendor
from vendortraining.models.serializers import vendorSerializer
from django.forms.models import model_to_dict
from rest_framework.authtoken.models import Token
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate
from django.contrib import auth
from vendortraining.models.serializers import userSerializer


from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK
)

class UserView(viewsets.ModelViewSet):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(UserView, self).dispatch(request, *args, **kwargs)
    
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.

    Additionally we also provide an extra `highlight` action.
    """
    queryset = UserInfo.objects.all()
    serializer_class = userSerializer.UserSerializer
    permission_classes = []

    '''
        @params detail
        @params methods 
        Get user object and all events associated with user
    '''
    @action(detail=False, methods=['post'])
    def profile(self, request, *args, **kwargs):
        return Response("Hi")
        user = User.objects.get(id=self.request.data.get('user_id'))
        user.events.all()
        token = Token.objects.get_or_create(user=user)

        try:
            res = userSerializer.UserSerializer(user)
            item = dict[res.data, token]
            return Response(item)
        except NameError:
            return Response(user, status=status.HTTP_404_NOT_FOUND)

    # deleting a user profile
    '''
        @params detail
        @params methods 
        Get user object and all events associated with user
    '''

    @action(detail=False, methods=['post'])
    def profileDelete(self, request, *args, **kwargs):
        user_name = request.data.get("username")
        user_password = request.data.get("password")
        try:
            # Ensure the suer is valid prior to deleting (Call auth_credentials from auth controller)
            user = auth.authenticate(request, username=user_name, password=user_password)
            # Get user
            authenticated_user = User.objects.get(id=user.id)
            authenticated_user.delete()
            user.delete()
            return Response("Successfully Deleted")
        except Exception:
            return Response("error")

# editing a user profile
# MAKE SURE TO USE THE RIGHT METHOD
    @action(detail=False, methods=['post'])
    def profileEdit(self, request, *args, **kwargs):
        user_name = request.data.get("username")
        user_password = request.data.get("password")
        #hash newPassword before storing it to user through set_password() function
        try:
            # Edit user information
            #user = auth.authenticate(request, username=user_name, password=user_password)
            authenticated_user = User.objects.get(id=user.id)
            authenticated_user.phone = request.data.get('phone')
            authenticated_user.email = request.data.get('email')
            authenticated_user.address = request.data.get('address')
            
            user.set_password(request.data.get('newPassword'))
            user.save()
            
            authenticated_user.save()
            return Response("Edit successful")
        except Exception:
            return Response("error")

# view events currently signed up for by the user
    @action(detail=False, methods=['post'])
    def userEvents(self, request, *args, **kwargs):
        queryset = Event.objects.filter(
            event_id=self.request.data.get('event_id'))
        serializer_class = eventSerializer.EventSerializer(queryset, many=true)
        return Response(serializer_class.data)

