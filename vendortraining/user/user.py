from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
# Create your views here.
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status, viewsets
from vendortraining.models import User
from vendortraining.models.serializers import userSerializer
from vendortraining.models import Event
from vendortraining.models.serializers import eventSerializer
from vendortraining.models import Vendor
from vendortraining.models.serializers import vendorSerializer
from django.forms.models import model_to_dict
from rest_framework.authtoken.models import Token
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate
from django.contrib import auth
from . import authetication

class UserView(viewsets.ModelViewSet):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(UserView, self).dispatch(request, *args, **kwargs)
    
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.

    Additionally we also provide an extra `highlight` action.
    """
    queryset = User.objects.all()
    serializer_class = userSerializer.UserSerializer
    permission_classes = []
    
    """ @action(detail=False, methods=['post'])
    def highlight(self, request, *args, **kwargs):
        queryset = User.objects.all()
        serializer_class = userSerializer.UserSerializer(queryset)
        return Response(serializer_class.data) """

# user seeing ALL listed events
    @action(detail=False, methods=['get'])
    def listAllEvents(self, request, *args, **kwargs):
        eventSet = Event.objects.all()
        serializer_class = eventSerializer.EventSerializer(eventSet, many=True)
        return Response(serializer_class.data)

# user seeing ONE event
    @action(detail=False, methods=['get'])
    def listEvent(self, request, *args, **kwargs):
        eventset = Event.objects.filter(id=self.request.data.get('event_id'))
        results = eventSerializer.EventSerializer(eventset)
        return Response(results.data)

# user joining ONE event. dont know if we should include the change to the attendance table somehow
    @action(detail=False, methods=['post'])
    def joinEvent(self, request, *args, **kwargs):
        queryset = Event.objects.filter(
            event_id=self.request.data.get('event_id'))
        serializer_class = eventSerializer.EventSerializer(queryset)
        return Response(serializer_class.data)

# reporting an event
    @action(detail=False, methods=['post'])
    def reportEvent(self, request, *args, **kwargs):
        queryset = Event.objects.filter(
            event_id=self.request.data.get('event_id'))
        serializer_class = eventSerializer.EventSerializer(queryset)
        return Response(serializer_class.data)

# reporting a vendor
    @action(detail=False, methods=['post'])
    def reportVendor(self, request, *args, **kwargs):
        queryset = Vendor.objects.filter(
            vendor_id=self.request.data.get('vendor_id'))
        serializer_class = vendorSerializer.VendorSerializer(
            queryset, many=True)
        return Response(serializer_class.data)

    @action(detail=False, methods=['post'])
    def profile(self, request, *args, **kwargs):
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
    @action(detail=False, methods=['post'])
    def profileDelete(self, request, *args, **kwargs):
        user_name = request.data.get("username")
        user_password = request.data.get("password")
        try:
            user = auth.authenticate(request, username=user_name, password=user_password)
            authenticated_user = User.objects.get(id=user.id)
            authenticated_user.delete()
            user.delete()
            return Response("Successfully Deleted")
        except Exception:
            return Exception

# editing a user profile
# MAKE SURE TO USE THE RIGHT METHOD
    @action(detail=False, methods=['get'])
    def profileEdit(self, request, *args, **kwargs):
        user = User.objects.filter(id=self.request.data.get('user_id'))
        user.email = request.data.get('email')
        return Response(res.data)

# view events currently signed up for by the user
    @action(detail=False, methods=['post'])
    def userEvents(self, request, *args, **kwargs):
        queryset = Event.objects.filter(
            event_id=self.request.data.get('event_id'))
        serializer_class = eventSerializer.EventSerializer(queryset, many=true)
        return Response(serializer_class.data)

    # view events currently signed up for by the user
    @action(detail=False, methods=['post'])
    #@csrf_exempt
    def login(self, request, *args, **kwargs):
        user_name = request.data.get("username")
        user_password = request.data.get("password")
        user_email = request.data.get('email')
        # authenticate user account.
        user = auth.authenticate(request, username=user_name, password=user_password)
        if user is not None:
            # login user account.
            authenticated_user = User.objects.get(id=user.id)
            auth.login(request, user)
            # Use authneticated user
            token = authetication.UserAuthetication.getToken(authenticated_user)
            serializer = userSerializer.UserSerializer(authenticated_user)
            obj = {
                #'user': user,
                'userData':serializer.data,
                'token':token
            }

            # set cookie to transfer user name to login success page.
            return Response(obj)
        else:
            error_json = {'error_message': 'User name or password is not correct.'}
            return Response(error_json)

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
                    new_user = User.objects.create(id=user.id, phone="123456789",role_id=1 )
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
            return Response( error_json)
