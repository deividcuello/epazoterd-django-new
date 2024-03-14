from rest_framework import serializers
from .models import Booking

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ["id", "phone", "date", "time", "time2", "booking_code", "additional_info", "people_no", "user"]