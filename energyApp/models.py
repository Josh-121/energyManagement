from django.db import models

class FloatData(models.Model):
    todayUsage = models.FloatField()
    monthUsage = models.FloatField()
    device1Usage = models.FloatField()
    device2Usage = models.FloatField()
    device3Usage = models.FloatField()

class BooleanData(models.Model):
    device1Switch = models.BooleanField()
    device2Switch = models.BooleanField()
    device3Switch = models.BooleanField()
