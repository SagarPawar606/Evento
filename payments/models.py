from django.db import models
from django.db.models.aggregates import Max
from events.models import Event
from django.contrib.auth.models import User

from django.core.exceptions import ValidationError
def exempt_zero(value):
    if value == 0:
        raise ValidationError(
            ('0 is not allowed please enter valid number'),
            params={'value': value},
        )

# Create your models here.
class Booking(models.Model):
    payment_status_choices = (
        (1, 'SUCCESS'),
        (2, 'FAILURE' ),
        (3, 'PENDING'),
    )
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    no_of_ticket = models.PositiveIntegerField(default=1, validators=[exempt_zero])
    total_amount = models.PositiveBigIntegerField(default=0)
    payment_date = models.DateTimeField(auto_now=True, null=True, blank=True)
    payment_status = models.IntegerField(choices = payment_status_choices, default=3)
    order_id = models.CharField(max_length=255, unique=True, null=True, blank=True)
    # razorpay attributes
    razorpay_order_id = models.CharField(max_length=500, null=True, blank=True)
    razorpay_payment_id = models.CharField(max_length=500, null=True, blank=True)
    razorpay_signature = models.CharField(max_length=500, null=True, blank=True)

    # class Meta:
    #     constraints = [
    #         models.UniqueConstraint(fields=['event', 'user'], name='event_booking')
    #     ]

    def save(self, *args, **kwargs, ):
        if self.order_id is None and self.payment_date and self.event.id and self.user.id:
            self.order_id = self.payment_date.strftime('EVT%Y%m%d%H%M%S') + str(self.event.id) + str(self.user.id)
        return super().save(*args, **kwargs)
