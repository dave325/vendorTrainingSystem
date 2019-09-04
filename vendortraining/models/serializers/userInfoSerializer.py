from rest_framework import serializers
from vendortraining.models import Role
from django.contrib.auth.models import User
class UserInfoSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id','username','first_name','last_name','email']
        depth = 2
    