# Generated by Django 3.2.9 on 2021-12-02 12:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0003_alter_booking_payment_date'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='booking',
            name='event_booking',
        ),
    ]
