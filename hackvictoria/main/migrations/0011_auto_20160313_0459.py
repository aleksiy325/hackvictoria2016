# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-13 11:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_trip_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trip',
            name='id',
        ),
        migrations.AddField(
            model_name='trip',
            name='key',
            field=models.AutoField(default=1, primary_key=True, serialize=False),
            preserve_default=False,
        ),
    ]
