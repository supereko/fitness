# Generated by Django 2.2.4 on 2019-10-24 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0003_auto_20191024_1125'),
    ]

    operations = [
        migrations.AddField(
            model_name='fitnessuser',
            name='height',
            field=models.PositiveSmallIntegerField(blank=True, null=True, verbose_name=' рост'),
        ),
        migrations.AlterField(
            model_name='fitnessuser',
            name='date_birth',
            field=models.DateField(blank=True, null=True, verbose_name='дата рождения'),
        ),
    ]
