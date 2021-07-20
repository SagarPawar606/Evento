from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import fields
from django.forms.formsets import MAX_NUM_FORM_COUNT
from .models import Profile


class UserRegisterForm(UserCreationForm):
    #bydefault Required->True
    full_name = forms.CharField(max_length=20)
    email = forms.EmailField(max_length=50)

    class Meta:
        model = User
        fields = ('username', 'full_name', 'email', 'password1', 'password2')


class UpdateUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields=['username', 'email',]

class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields=['profile_pic', 'bio', 'location', 'insta', 'twitter', 'facebook', 'website']