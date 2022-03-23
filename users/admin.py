from django.contrib import admin
from .models import Profile, Pocket, PocketEvent

# Register your models here.

class ProfileInterface(admin.ModelAdmin):
    list_display = ('id', 'user')

class PocketEventInterface(admin.ModelAdmin):
    list_display = ('id', 'pocket', 'event')

class PocketInterface(admin.ModelAdmin):
    list_display = ('id', 'pocket_user')



admin.site.register(Profile, ProfileInterface)
admin.site.register(Pocket, PocketInterface)
admin.site.register(PocketEvent, PocketEventInterface)
