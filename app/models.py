from django.db import models

class Birth(models.Model):
    county = models.CharField(max_length=200)
    y2005 = models.IntegerField(default=0)
    y2006 = models.IntegerField(default=0)
    y2007 = models.IntegerField(default=0)
    y2008 = models.IntegerField(default=0)
    y2009 = models.IntegerField(default=0)
    y2010 = models.IntegerField(default=0)
    y2011 = models.IntegerField(default=0)
    y2012 = models.IntegerField(default=0)
    y2013 = models.IntegerField(default=0)
    y2014 = models.IntegerField(default=0)
    y2015 = models.IntegerField(default=0)


class dokmeta(models.Model):
    kood = models.CharField(max_length=255)
    korpus = models.CharField(max_length=255)
    tekstikeel = models.CharField(max_length=25)
    tekstityyp = models.CharField(max_length=25)
    elukoht = models.CharField(max_length=25)
    taust = models.CharField(max_length=25)
    vanus = models.CharField(max_length=25)
    sugu = models.CharField(max_length=10)
    emakeel = models.CharField(max_length=25)
    kodukeel = models.CharField(max_length=25)
    keeletase = models.CharField(max_length=5)
    haridus = models.CharField(max_length=10)
    abivahendid = models.CharField(max_length=10)
    
class dokarvud(models.Model):
    kood = models.CharField(max_length=30, primary_key=True)
    tahti = models.IntegerField(default=0)
    sonu = models.IntegerField(default=0)
    lauseid = models.IntegerField(default=0)
    vigu = models.IntegerField(default=0)
    veatyype = models.IntegerField(default=0)
    kolmetahelistepr = models.FloatField(default=0)
    viietahelistepr = models.FloatField(default=0)
    kymnejarohkemtahelistepr = models.FloatField(default=0)
    kahesonalistepr = models.FloatField(default=0)
    kolmesonalistepr = models.FloatField(default=0)
    kuuekuni9sonalistepr = models.FloatField(default=0)
    kymnekuni20sonalistepr = models.FloatField(default=0)

class Calories(models.Model):
    food_item = models.CharField(max_length=200)
    calories = models.IntegerField(default=0)

class Diary(models.Model):
    user = models.CharField(max_length=200)
    food_item = models.CharField(max_length=200)
    amount = models.IntegerField(default=0)
    calories = models.IntegerField(default=0)
    date_added = models.DateField(blank=True, null=True)

