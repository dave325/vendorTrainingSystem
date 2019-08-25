from rest_framework import serializers
from django.contrib.auth.models import User
from vendortraining.models.serializers import userInfoSerializer
from vendortraining.models import UserInfo

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','username','first_name','last_name']
        depth = 2
  
    def getUserInfo(self,id):
        return userInfoSerializer.UserInfoSerializer(UserInfo.objects.get(id=id)).data