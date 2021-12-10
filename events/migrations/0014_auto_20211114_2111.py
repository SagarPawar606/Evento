# Generated by Django 3.2.9 on 2021-11-14 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0013_auto_20210705_1644'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='pricing',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='keywords',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
