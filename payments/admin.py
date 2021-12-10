from django.contrib import admin
from .models import Booking
# Register your models here.

class BookingInterface(admin.ModelAdmin):
    list_display = ('user', 'event' ,'order_id', 'payment_date', 'payment_status')

admin.site.register(Booking, BookingInterface)