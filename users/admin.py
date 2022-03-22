from django.contrib import admin
from .models import Profile, Pocket

# Register your models here.

class ProfileInterface(admin.ModelAdmin):
    list_display = ('id', 'user')

class PocketInterface(admin.ModelAdmin):
    list_display = ('id', 'user', 'event')


admin.site.register(Profile, ProfileInterface)
admin.site.register(Pocket, PocketInterface)