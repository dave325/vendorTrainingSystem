from rest_framework import serializers
from vendortraining.models import Role

class RoleSerializer(serializers.Serializer):
    class Meta:
        model = Role
        fields = '__all__'
        depth = 2