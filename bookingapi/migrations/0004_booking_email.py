# Generated by Django 4.2.7 on 2024-03-12 05:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookingapi', '0003_booking_booking_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='email',
            field=models.CharField(default='', max_length=255),
        ),
    ]