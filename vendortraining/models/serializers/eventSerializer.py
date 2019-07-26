from rest_framework import serializers
from vendortraining.models import Event


class EventSerializer(serializers.Serializer):
    event_id = serializers.IntegerField()
    vendor_id= serializers.IntegerField()
    created_by= serializers.IntegerField()
    modified_by= serializers.IntegerField()
    modified_at= serializers.DateField()
    created_at= serializers.DateField()