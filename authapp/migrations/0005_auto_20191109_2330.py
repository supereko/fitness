# Generated by Django 2.2.7 on 2019-11-09 23:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0004_auto_20191024_1242'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fitnessuser',
            name='antropometry',
        ),
        migrations.RemoveField(
            model_name='fitnessuser',
            name='schedule',
        ),
    ]
