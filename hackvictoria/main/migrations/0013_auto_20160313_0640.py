# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-13 13:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_auto_20160313_0608'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='user',
            field=models.CharField(max_length=200),
        ),
    ]
