# Generated by Django 3.2.9 on 2021-11-14 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0014_auto_20211114_2111'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='pricing',
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
    ]
