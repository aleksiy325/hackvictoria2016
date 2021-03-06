# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-13 02:20
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Trip',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(null=True)),
                ('date_posted', models.DateTimeField(null=True)),
                ('active', models.BooleanField(default=True)),
                ('num_passengers', models.IntegerField(default=0)),
                ('msg', models.CharField(max_length=200)),
                ('looktype', models.CharField(choices=[('Driver', 'D'), ('Passenger', 'P')], default=('Driver', 'D'), max_length=200)),
                ('destination', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='location_dest', to=settings.AUTH_USER_MODEL)),
                ('origin', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='location_origin', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='userprofile',
            name='age',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='joined',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='location',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='type',
            field=models.CharField(choices=[('Driver', 'D'), ('Passenger', 'P')], default=('Driver', 'D'), max_length=200),
        ),
    ]
