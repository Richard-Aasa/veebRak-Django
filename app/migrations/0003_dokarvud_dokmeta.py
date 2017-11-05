# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-05 16:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20171105_0915'),
    ]

    operations = [
        migrations.CreateModel(
            name='dokarvud',
            fields=[
                ('kood', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('tahti', models.IntegerField(default=0)),
                ('sonu', models.IntegerField(default=0)),
                ('lauseid', models.IntegerField(default=0)),
                ('vigu', models.IntegerField(default=0)),
                ('veatyype', models.IntegerField(default=0)),
                ('kolmetahelistepr', models.FloatField(default=0)),
                ('viietahelistepr', models.FloatField(default=0)),
                ('kymnejarohkemtahelistepr', models.FloatField(default=0)),
                ('kahesonalistepr', models.FloatField(default=0)),
                ('kolmesonalistepr', models.FloatField(default=0)),
                ('kuuekuni9sonalistepr', models.FloatField(default=0)),
                ('kymnekuni20sonalistepr', models.FloatField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='dokmeta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kood', models.CharField(max_length=255)),
                ('korpus', models.CharField(max_length=255)),
                ('tekstikeel', models.CharField(max_length=25)),
                ('tekstityyp', models.CharField(max_length=25)),
                ('elukoht', models.CharField(max_length=25)),
                ('taust', models.CharField(max_length=25)),
                ('vanus', models.CharField(max_length=25)),
                ('sugu', models.CharField(max_length=10)),
                ('emakeel', models.CharField(max_length=25)),
                ('kodukeel', models.CharField(max_length=25)),
                ('keeletase', models.CharField(max_length=5)),
                ('haridus', models.CharField(max_length=10)),
                ('abivahendid', models.CharField(max_length=10)),
            ],
        ),
    ]