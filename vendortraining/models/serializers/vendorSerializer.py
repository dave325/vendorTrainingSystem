from rest_framework import serializers
from vendortraining.models import Vendor

#vendor is considered deleted if address, phone, and email is blank
class VendorSerializer(serializers.ModelSerializer):
    class Meta:
        model= Vendor
        fields= '__all__'