from rest_framework import serializers
from vendortraining.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields =["id", "email", "first_name", "last_name", "role_id", "phone", "address", "public", "password"]