from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.conf import settings

class Booking(models.Model):

    phone = models.CharField(max_length=255, blank=False, null=False, default='')
    date = models.CharField(max_length=255, blank=False, null=False, default='')
    email = models.CharField(max_length=255, blank=False, null=False, default='')
    time = models.CharField(max_length=255, blank=False, null=False, default='')
    time2 = models.CharField(max_length=255, blank=False, null=False, default='')
    booking_code = models.CharField(max_length=255, blank=False, null=False, default='')
    people_no = models.CharField(max_length=10, blank=False, null=False, default='')
    additional_info = models.CharField(max_length=255, blank=False, null=False, default='')
    created_at = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE, blank = True, null = True)
    