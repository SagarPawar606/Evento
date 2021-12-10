from django import forms
from django.forms import widgets
from .models import Booking


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['no_of_ticket']
        widgets = {
            'no_of_ticket' : forms.NumberInput(attrs={'class':'col-sm'}),
        }