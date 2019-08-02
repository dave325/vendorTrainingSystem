from rest_framework import serializers
from vendortraining.models import Attendance

class AttendanceSerializer(serializers.Serializer):
    class Meta:
        model: Attendance
        fields: '__all__'
