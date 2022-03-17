from django.contrib import admin
from .models import Event
# Register your models here.

class EventInterface(admin.ModelAdmin):
    list_display = ('id', 'title', 'publisher', 'event_date', 'featured', 'disabled')

admin.site.register(Event, EventInterface)
