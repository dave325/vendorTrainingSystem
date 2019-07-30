from rest_framework import serializers
from vendortraining.models import Member

class MemberSerializer(serializers.Serializer):
    user_id = serializers.IntegerField()
    vendor_id = serializers.IntegerField()
    company_role = serializers.CharField(max_length=100, min_length=None)