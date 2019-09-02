from rest_framework import serializers
from vendortraining.models import Member, UserInfo
from vendortraining.models.serializers import vendorSerializer, userInfoSerializer

class MemberSerializer(serializers.ModelSerializer):
    #Test
    user = userInfoSerializer.UserInfoSerializer(many=False, read_only=True)
    #serializer information 
    class Meta:
        model = Member
        fields = ['company_role', 'vendor_id', 'user']
        depth = 1