# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-18 11:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('me', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='snippet',
            options={},
        ),
        migrations.RemoveField(
            model_name='snippet',
            name='idno',
        ),
        migrations.AddField(
            model_name='snippet',
            name='id',
            field=models.AutoField(auto_created=True, default=0, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
    ]