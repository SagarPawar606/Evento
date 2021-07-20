# Generated by Django 3.2 on 2021-04-23 04:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='featurned',
            new_name='featured',
        ),
        migrations.AlterField(
            model_name='event',
            name='event_banner_img',
            field=models.ImageField(blank=True, upload_to='events_banner/'),
        ),
    ]
