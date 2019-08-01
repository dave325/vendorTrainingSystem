from vendortraining.models import User
from django.contrib.auth.models import User
from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.decorators import action


class UserAuthetication(viewsets.ViewSet):
    
    queryset = User.objects.all()
    @action(detail=False, methods=['post'])
    def checkUser(self, request, *args, **kwargs):
        user = User.objects.get(id=self.request.data.get('user_id'))
        if self.request.data.get('user_id') == "1ß":
            return True
        else:
            return False  
    @action(detail=False, methods=['post'])
    def checkId(self, request, *args, **kwargs):
        if User.objects.filter(id == self.request.data.get('user_id')):
            return True
        else:
            return False
