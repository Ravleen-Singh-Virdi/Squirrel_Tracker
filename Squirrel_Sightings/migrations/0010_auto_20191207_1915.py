# Generated by Django 2.2.7 on 2019-12-07 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Squirrel_Sightings', '0009_auto_20191207_1914'),
    ]

    operations = [
        migrations.AlterField(
            model_name='squirrels',
            name='Other_Activities',
            field=models.CharField(default=None, help_text='Other activities', max_length=100),
        ),
    ]
