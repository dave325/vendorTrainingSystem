from rest_framework import serializers
from vendortraining.models import User

class UserSerializer(serializers.ModelSerializer):
    roleid = serializers.PrimaryKeyRelatedField( read_only=True)
    class Meta:
        model = User
        fields = '__all__'
        depth = 2