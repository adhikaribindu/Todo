from rest_framework import serializers
from attendance.models import Attendance
from django.contrib.auth import get_user_model

User=get_user_model()
class AttendanceSerializers(serializers.ModelSerializer):
    class Meta:
        model=Attendance 
        fields=(
            "user_name",
            "checkin_date",
            "check_in",
            "check_out"
        )

class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=[
            "first_name",
            "last_name",
            "email"
        ]