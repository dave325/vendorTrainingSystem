from rest_framework import serializers
from vendortraining.models import Role

class roleSerializer(serializers.Serializer):
    role_id = serializers.IntegerField()
    role_name = serializers.CharField(max_length=45, min_length=None)
