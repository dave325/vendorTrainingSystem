from rest_framework import serializers
from vendortraining.models import UserInfo, Vendor, Member, Event, Role
from django.contrib.auth.models import User
from vendortraining.models.serializers import userInfoSerializer, vendorSerializer, eventSerializer

class UserSerializer(serializers.ModelSerializer):
    user = userInfoSerializer.UserInfoSerializer(many=False, read_only=True)
    class Meta:
        model = UserInfo
        fields = ['id', 'phone','address','public','role_id','user']
        depth = 2
  
    def getUserInfo(self,id):
        return userInfoSerializer.UserInfoSerializer(UserInfo.objects.get(id=id)).data
