# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-13 11:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_trip_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='trip',
            name='user',
            field=models.CharField(default='aleksiy', max_length=200),
            preserve_default=False,
        ),
    ]
