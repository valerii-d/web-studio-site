# Generated by Django 2.2.5 on 2019-10-08 19:31

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('user_profile', '0005_auto_20190929_1320'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='managers',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]
