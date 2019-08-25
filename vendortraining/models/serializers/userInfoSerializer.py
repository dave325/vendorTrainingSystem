from rest_framework import serializers
from vendortraining.models import UserInfo
from vendortraining.models import Role
class UserInfoSerializer(serializers.ModelSerializer):
    role_id = serializers.PrimaryKeyRelatedField(read_only='True')

    class Meta:
        model = UserInfo
        fields = '__all__'
        depth = 2
    