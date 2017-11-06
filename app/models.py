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

class Calories(models.Model):
    food_item = models.CharField(max_length=200)
    calories = models.IntegerField(default=0)

class Diary(models.Model):
    user = models.CharField(max_length=200)
    food_item = models.CharField(max_length=200)
    amount = models.IntegerField(default=0)
    calories = models.IntegerField(default=0)
    date_added = models.DateField(blank=True, null=True)
