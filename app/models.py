from django.db import models

class Births(models.Model):
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

