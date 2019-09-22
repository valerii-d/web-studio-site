# Generated by Django 2.2.5 on 2019-09-22 19:16

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0003_auto_20190922_1539'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='paid',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='order',
            name='deadline',
            field=models.DateTimeField(default=datetime.datetime(2019, 9, 22, 19, 16, 5, 861025, tzinfo=utc)),
        ),
    ]
