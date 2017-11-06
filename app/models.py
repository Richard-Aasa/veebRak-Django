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
    
class raamatud(models.Model):
    raamatu_nr = models.IntegerField(default=0, primary_key=True)
    raamatu_nimi = models.CharField(max_length=255)
    raamatu_lehti = models.IntegerField(default=0)
    omanikud = models.ManyToManyField("omanikud")
    
class omanikud(models.Model):
    id = models.IntegerField(primary_key=True)
    omaniku_nr = models.IntegerField(default=0)
    omanik_nimi = models.CharField(max_length=255)
    omatud_raamatu_nr = models.IntegerField()