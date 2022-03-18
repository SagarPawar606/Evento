from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from PIL import Image
from django.urls import reverse

from ckeditor.fields import RichTextField

# Create your models here.

class Event(models.Model):
    category = [
        ('convention', 'Convention'),
        ('tech', 'Technology'),
        ('charity', 'Charity & Fundraising Event'),
        ('seminar', 'Seminar'),
        ('workshop_education', 'Workshop/Education'),
        ('sport_outdoor', 'Sports/Outdoor Activity'),
        ('art_entertain', 'Art & Entertainment'),
        ('concert', 'Concert'),
    ]
 
    category.sort()
    category.append(('other', 'Other'))

    title = models.CharField(max_length=200, unique=True)
    description = RichTextField()
    venue = models.TextField()
    city = models.CharField(max_length=100, null=True, blank=True)
    event_category = models.CharField(max_length=20, choices=category)
    publisher = models.ForeignKey(User, on_delete = models.CASCADE)
    event_banner_img = models.ImageField(upload_to = 'events_banner/')
    date_added = models.DateField(auto_now_add=True,)   
    event_date = models.DateField(blank=True, null=True)
    pricing = models.IntegerField(blank=True, null=True, default=0)
    keywords = models.CharField(max_length=200, blank=True)

    featured = models.BooleanField(default=False)
    disabled = models.BooleanField(default=False)

    class Meta:
        ordering = ["-date_added"]

    # Override the default save method of models
    # We can make changes and then save the object in model 
    def save(self):
        if self.city:
            self.city = self.city.lower()
        super().save()
        img = Image.open(self.event_banner_img.path)
        if img.height>800 or img.width>500:
            dimension = (800,500)
            img.thumbnail(dimension)
            img.save(self.event_banner_img.path)

    def get_absolute_url(self):
        return reverse('event-detail', kwargs={'pk': self.pk})


    def __str__(self):
        return f'{self.title} - {self.publisher}'


