# Generated by Django 2.2.5 on 2019-09-29 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0004_auto_20190929_1316'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='deadline',
            field=models.DateTimeField(),
        ),
    ]