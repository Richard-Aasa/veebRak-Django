# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-06 15:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Birth',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('county', models.CharField(max_length=200)),
                ('y2005', models.IntegerField(default=0)),
                ('y2006', models.IntegerField(default=0)),
                ('y2007', models.IntegerField(default=0)),
                ('y2008', models.IntegerField(default=0)),
                ('y2009', models.IntegerField(default=0)),
                ('y2010', models.IntegerField(default=0)),
                ('y2011', models.IntegerField(default=0)),
                ('y2012', models.IntegerField(default=0)),
                ('y2013', models.IntegerField(default=0)),
                ('y2014', models.IntegerField(default=0)),
                ('y2015', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='omanikud',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('omaniku_nr', models.IntegerField(default=0)),
                ('omanik_nimi', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='raamatud',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('raamatu_nr', models.IntegerField(default=0)),
                ('raamatu_nimi', models.CharField(max_length=254)),
                ('raamatu_lehti', models.IntegerField(default=0)),
            ],
        ),
        migrations.AddField(
            model_name='omanikud',
            name='omatud_raamatu_nr',
            field=models.ManyToManyField(to='app.raamatud'),
        ),
    ]
