# Generated by Django 5.0.2 on 2024-02-12 22:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('weather', '0002_rename_data_id_weatherdata_weather_data_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='weatherdata',
            old_name='state',
            new_name='city',
        ),
    ]
