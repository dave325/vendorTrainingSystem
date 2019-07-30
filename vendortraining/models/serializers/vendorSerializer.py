from rest_framework import serializers
from vendortraining.models import Vendor

#vendor is considered deleted if address, phone, and email is blank
class VendorSerializer(serializers.Serializer):
    vendor_id = serializers.IntegerField()
    name = serializers.CharField(max_length=100, min_length=None)
    address = serializers.TextField(max_length=254, min_length=None, allow_blank=True)
    phone = serializers.CharField(max_length=100, min_length=None, allow_blank=True)
    email = serializers.EmailField(max_length=254, min_length=None, allow_blank=True)
    isApproved = serializers.BooleanField()