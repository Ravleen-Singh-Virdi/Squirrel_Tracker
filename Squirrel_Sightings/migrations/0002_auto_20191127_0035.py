# Generated by Django 2.2.7 on 2019-11-27 00:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Squirrel_Sightings', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='squirrels',
            name='Location',
            field=models.CharField(choices=[('ground plane', ' Ground Plane'), ('above ground', 'Above Ground'), ('other', 'Other')], default='other', help_text='Location of the Squirrel', max_length=100),
        ),
        migrations.AddField(
            model_name='squirrels',
            name='Specific_Location',
            field=models.CharField(default=None, help_text='Specific Location', max_length=30),
            preserve_default=False,
        ),
    ]
