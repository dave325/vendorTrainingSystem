from rest_framework import serializers
from vendortraining.models import Member

class memberSerializer(serializers.Serializer):
    user_id = serializers.IntegerField()
    vendor_id = serializers.IntegerField()
    company_role = serializers.CharField(max_length=45, min_length=None)