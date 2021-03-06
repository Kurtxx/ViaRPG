# Generated by Django 2.1.2 on 2018-11-26 19:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Resources',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stat_str', models.IntegerField(default=0)),
                ('stat_vit', models.IntegerField(default=0)),
                ('stat_dex', models.IntegerField(default=0)),
                ('stat_money', models.IntegerField(default=0)),
                ('stat_food', models.IntegerField(default=0)),
                ('stat_energy', models.IntegerField(default=0)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
