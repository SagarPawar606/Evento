# Generated by Django 2.1 on 2021-06-19 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0004_auto_20210619_1809'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='eventcontroler',
            name='event',
        ),
        migrations.AddField(
            model_name='event',
            name='disabled',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='event',
            name='featured',
            field=models.BooleanField(default=False),
        ),
        migrations.DeleteModel(
            name='EventControler',
        ),
    ]
