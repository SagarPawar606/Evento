from django import forms
from django.forms import widgets
from .models import Event



class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['title', 'event_category','event_banner_img', 'description', 'venue', 'pricing' ,'event_date', 'keywords']
        widgets={
            'title' : forms.TextInput(attrs={'placeholder':'Title'}),
            'description' : forms.Textarea(attrs={'placeholder':'Event Details'}),
            'venue' : forms.Textarea(attrs={'cols':6, 'rows':3, 'placeholder':'Address'}), 
            'pricing' : forms.TextInput(attrs={'placeholder': 'leave it blank, if its \'Free\' event'}),
            #'event_date' : forms.DateInput(format='%d/%m/%Y' , attrs={'placeholder':'dd/mm/yyyy'}),
            'keywords' : forms.TextInput(attrs={'placeholder':'Add keywords related to your event'}),
            'event_date': widgets.SelectDateWidget()
        }
    # event_date = forms.DateField(
    #     widget=forms.DateInput(format='%d/%m/%Y', attrs={'placeholder':'dd/mm/yyyy'}, ),
    #     input_formats=('%d/%m/%Y',)
    #     ) 

