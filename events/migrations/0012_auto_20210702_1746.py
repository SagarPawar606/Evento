# Generated by Django 2.1 on 2021-07-02 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0011_auto_20210630_1654'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='event_banner_img',
            field=models.ImageField(upload_to='events_banner/'),
        ),
    ]
