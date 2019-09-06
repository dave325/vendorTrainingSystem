from rest_framework import serializers
from vendortraining.models import Member
from vendortraining.models.serializers import vendorSerializer, userSerializer

class MemberSerializer(serializers.ModelSerializer):
    #Test
    user = userSerializer.UserSerializer(many=False, read_only=True)
    #serializer information 
    class Meta:
        model = Member
        fields = ['company_role', 'vendor_id', 'user']
        depth = 1