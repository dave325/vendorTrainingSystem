from rest_framework import serializers
from vendortraining.models import Event


class EventSerializer(serializers.Serializer):
    class Meta:
        model: Event
        fields: '__all__'