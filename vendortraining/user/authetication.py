from vendortraining.models import User
from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from vendortraining.models.serializers import userSerializer



class UserAuthetication(viewsets.ModelViewSet):
    
    queryset = User.objects.all()
    @action(detail=False, methods=['post'])
    def checkUser(self, request, *args, **kwargs):
        user = User.objects.get(id = self.request.data.get('user_id'))
        res = userSerializer.UserSerializer(user)
        if self.request.data.get('user_id') == 5:
            return res.data
        else:
            return False  
    @action(detail=False, methods=['post'])
    def checkId(self, request, *args, **kwargs):
        if User.objects.filter(id == self.request.data.get('user_id')):
            return True
        else:
            return False
