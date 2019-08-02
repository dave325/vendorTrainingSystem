from rest_framework import serializers
from vendortraining.models import Member

class MemberSerializer(serializers.Serializer):
    class Meta:
        model: Member
        fields: '__all__'