# Generated by Django 2.1.2 on 2018-11-30 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_resources'),
    ]

    operations = [
        migrations.AddField(
            model_name='resources',
            name='stat_lvl',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='resources',
            name='stat_maxexp',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='resources',
            name='stat_minexp',
            field=models.IntegerField(default=0),
        ),
    ]
