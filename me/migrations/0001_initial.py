# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-16 13:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Snippet',
            fields=[
                ('idno', models.IntegerField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(blank=True, default='', max_length=100)),
                ('last_name', models.CharField(blank=True, default='', max_length=100)),
                ('phone_number', models.CharField(max_length=12)),
                ('email', models.EmailField(max_length=100)),
                ('role', models.CharField(choices=[('ADMIN', 'admin'), ('REGULAR', 'Reg')], default='REGULAR', max_length=100)),
            ],
            options={
                'ordering': ('idno',),
            },
        ),
    ]
