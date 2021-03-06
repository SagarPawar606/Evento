# Generated by Django 2.1 on 2021-07-05 11:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0013_auto_20210705_1644'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '0005_auto_20210628_1733'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pocket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.Event')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='pocket',
            unique_together={('user', 'event')},
        ),
    ]
