# Generated by Django 3.2.9 on 2021-12-01 11:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import payments.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('events', '0016_auto_20211115_1750'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('no_of_ticket', models.PositiveIntegerField(default=1, validators=[payments.models.exempt_zero])),
                ('payment_date', models.DateTimeField(auto_now_add=True)),
                ('payment_status', models.IntegerField(choices=[(1, 'SUCCESS'), (2, 'FAILURE'), (3, 'PENDING')], default=3)),
                ('order_id', models.CharField(blank=True, max_length=255, null=True, unique=True)),
                ('razorpay_order_id', models.CharField(blank=True, max_length=500, null=True)),
                ('razorpay_payment_id', models.CharField(blank=True, max_length=500, null=True)),
                ('razorpay_signature', models.CharField(blank=True, max_length=500, null=True)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.event')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddConstraint(
            model_name='booking',
            constraint=models.UniqueConstraint(fields=('event', 'user'), name='event_booking'),
        ),
    ]
