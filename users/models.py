from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields import BLANK_CHOICE_DASH
from PIL import Image
from events.models import Event
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(upload_to='profile_pics', default='default_pic.jpg')
    bio = models.TextField(blank=True)
    location = models.CharField(max_length=100, blank=True)
    insta = models.CharField(max_length=100, blank=True)
    twitter = models.CharField(max_length=100, blank=True)
    facebook = models.CharField(max_length=100, blank=True)
    website = models.CharField(max_length=100, blank=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.profile_pic.path)
        if img.height>300 or img.width>300:
            dimension = (300,300)
            img.thumbnail(dimension)
            img.save(self.profile_pic.path)

    def __str__(self):
        return self.user.username + '- Profile'
'''
class Pocket(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=False, null=False)
    event = models.ForeignKey(Event, on_delete=models.CASCADE, blank=False, null=False)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['user', 'event'], name='unique_event')
        ]

    def __str__(self):
        return f'{self.user.username} - {self.event.title}'
'''

class Pocket(models.Model):
    pocket_user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.pocket_user.username} - Pocket'

class PocketEvent(models.Model):
    pocket = models.ForeignKey(Pocket, on_delete=models.CASCADE) 
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['pocket', 'event'], name='unique_event')
        ]
    
    def __str__(self):
        return f'{self.pocket} - {self.event.title}'