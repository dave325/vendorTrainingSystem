from rest_framework import serializers
from vendortraining.models import Event


class EventSerializer(serializers.Serializer):
    #vendor_id = serializers.IntegerField()
    #created_by = serializers.CharField()
    #created_at = serializers.DateField()
    #modified_by = serializers.CharField()
    #modified_at = serializers.DateField()
    #is_approved = serializers.BooleanField()
    #total_attendance = serializers.IntegerField()
    class Meta:
        model: Event
        fields: '__all__'