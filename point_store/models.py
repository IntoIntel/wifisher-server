from django.contrib.gis.db import models 

class DataPoint(models.Model):
    #localization
    position = models.PointField()
    speed = models.FloatField()
    accuracy = models.FloatField()
    altitude = models.FloatField()
    time = models.DateTimeField()
    #wifi
    frequency = models.IntegerField()
    level = models.IntegerField()
    ssid = models.CharField(max_length=300)
    bssid = models.CharField(max_length=300)
    capabilities = models.TextField()
    
    objects = models.GeoManager();
    