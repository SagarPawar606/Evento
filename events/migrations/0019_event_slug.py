# Generated by Django 3.2.9 on 2022-03-23 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0018_alter_event_pricing'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='slug',
            field=models.SlugField(default='djangodbmodelsfieldscharfield', max_length=100),
        ),
    ]
