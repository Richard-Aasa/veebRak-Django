# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-06 15:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='raamatud',
            name='raamatu_nimi',
            field=models.CharField(max_length=255),
        ),
    ]