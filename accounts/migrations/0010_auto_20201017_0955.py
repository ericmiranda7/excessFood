# Generated by Django 3.1.2 on 2020-10-17 04:25

import django.contrib.gis.db.models.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0009_merge_20201017_0953'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='donator',
            name='lat',
        ),
        migrations.RemoveField(
            model_name='donator',
            name='lon',
        ),
        migrations.AddField(
            model_name='donator',
            name='location',
            field=django.contrib.gis.db.models.fields.PointField(blank=True, null=True, srid=4326),
        ),
    ]