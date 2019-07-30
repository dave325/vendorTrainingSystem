from rest_framework import serializers
from vendortraining.models import Vendor

class VendorSerializer(serializers.Serializer):
    vendor_id = serializers.IntegerField()
    name = serializers.CharField(max_length=45, min_length=None)
    address = serializers.CharField(max_length=45, min_length=None, allow_blank=False)
    phone = serializers.CharField(max_length=45, min_length=None, allow_blank=False)
    email = serializers.CharField(max_length=45, min_length=None, allow_blank=False)
    isApproved = serializers.BooleanField()