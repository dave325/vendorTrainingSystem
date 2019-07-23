from rest_framework import serializers
from vendortraining.models import User

class userSerializer(serializers.Serializer):
    user_id=serializers.IntegerField()
    email=serializers.CharField(max_length=45, min_length=None)
    first_name=serializers.CharField(max_length=45, min_length=None)
    last_name=serializers.CharField(max_length=45, min_length=None)
    role_id=serializers.IntegerField()
    phone=serializers.CharField(max_length=45, min_length=None)
    address=serializers.CharField(max_length=128, min_length=None)
    public=serializers.BooleanField()
    password=serializers.CharField(max_length=128, min_length=None)