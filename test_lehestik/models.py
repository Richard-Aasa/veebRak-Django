from django.db import models


class Dok_Meta(models.Model):
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
