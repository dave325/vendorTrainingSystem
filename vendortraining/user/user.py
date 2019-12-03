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
    # deleting a user profile
    '''
        @params detail
        @params methods 
        Get user object and all events associated with user
    '''

    # TODO: should be in super
    # TODO: check for vendor and member
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
    # TODO: should be in super
    @action(detail=False, methods=['post'])
    def profileEdit(self, request, *args, **kwargs):
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





    #TODO: MOVED FROM VENDOR. MAKE SUR THIS WORKS -ED
    #TODO Peter: it shows no error message when invalid input is given 
    @action(detail=False, methods=['post'])
    def editMyProfile(self, request, *args, **kwargs):
        vendorProfile = Vendor.objects.filter(vendor_id = self.request.data.get('vendor_id'))
        y = ""
        d = {}
        for x in self.request.data:
            if len(str(self.request.data.get(x))) == 0: #If the data field is empty, we assume that we do not want to update that value----How it works:We convert to str to use len(). Probably a more elegent way of doing this though
                continue
            d[x] = self.request.data.get(x)
            # x = str(self.request.data.get(x))
            # y = y + " " + x

        vendorProfile.update(**d)

        return Response(y) # for debug-- not nessicary
