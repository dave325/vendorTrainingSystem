from vendortraining.models import user
from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from vendortraining.models.serializers import userSerializer

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from rest_framework import permissions 


#jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
#jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

class UserAuthetication(viewsets.ModelViewSet):
    
    queryset = User.objects.all()
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
        username = request.data.get("username", "")
        password = request.data.get("password", "")
        baseUser = authenticate(request, username=username, password=password)
        if baseUser is not None:
            # login saves the user’s ID in the session,
            # using Django’s session framework.
            login(request, baseUser)
            serializer = TokenSerializer(data={
                # using drf jwt utility functions to generate a token
                "token": jwt_encode_handler(
                    jwt_payload_handler(baseUser)
                )})
            serializer.is_valid()
            return Response(serializer.data)
        return Response(status=status.HTTP_401_UNAUTHORIZED)
    