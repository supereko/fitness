# Generated by Django 2.2.7 on 2019-11-10 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0004_auto_20191109_2330'),
    ]

    operations = [
        migrations.RenameField(
            model_name='schedule',
            old_name='visit',
            new_name='is_visit',
        ),
        migrations.AddField(
            model_name='schedule',
            name='date',
            field=models.DateField(blank=True, null=True, verbose_name='дата посещения тренировки'),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='time',
            field=models.TimeField(blank=True, null=True, verbose_name='время посещения тренировки'),
        ),
    ]
