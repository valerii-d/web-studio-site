# Generated by Django 2.2.5 on 2019-10-09 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0003_auto_20191009_1241'),
    ]

    operations = [
        migrations.AlterField(
            model_name='manager',
            name='bio',
            field=models.TextField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='manager',
            name='location',
            field=models.CharField(max_length=30, null=True),
        ),
    ]
