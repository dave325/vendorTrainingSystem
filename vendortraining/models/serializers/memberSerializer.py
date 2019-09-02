from rest_framework import serializers
from vendortraining.models import Member
from vendortraining.models.serializers import vendorSerializer

class MemberSerializer(serializers.ModelSerializer):

    class Meta:
        model= Member
        fields= ['company_role', 'vendor_id']
        depth= 2