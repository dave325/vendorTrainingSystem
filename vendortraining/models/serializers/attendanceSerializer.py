from rest_framework import serializers
from vendortraining.models import Attendance

class AttendanceSerializer(serializers.Serializer):
    attendance_id = serializers.IntegerField()
    user_id = serializers.IntegerField()
    event_id = serializers.IntegerField()
