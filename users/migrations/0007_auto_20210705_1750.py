# Generated by Django 3.2.5 on 2021-07-05 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_auto_20210705_1715'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='pocket',
            unique_together=set(),
        ),
        migrations.AddConstraint(
            model_name='pocket',
            constraint=models.UniqueConstraint(fields=('user', 'event'), name='unique_event'),
        ),
    ]
