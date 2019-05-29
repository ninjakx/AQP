from django.conf import settings

from django.db import models

class Data(models.Model):
   
    Year =  models.IntegerField(blank=False)
    RPD_deaths =  models.IntegerField(blank=False)
    Total_deaths =  models.IntegerField(blank=False)
    Four_wheelers =  models.IntegerField(blank=False)
    Two_wheelers =  models.IntegerField(blank=False)
    Auto_rickshaw =  models.IntegerField(blank=False)
    Buses =  models.IntegerField(blank=False)
    Taxis =  models.IntegerField(blank=False)
    Good_vehicles =  models.IntegerField(blank=False)
    Total_vehicles =  models.IntegerField(blank=False)
    Population =  models.IntegerField(blank=False)
    
    
    def __str__(self):
        return str(self.Year)

class pol(models.Model):
    Station_Name = models.IntegerField(blank=False)
    Ammonia = models.CharField(max_length=30,blank=False)
    Carbon_Monoxide = models.CharField(max_length=30,blank=False)
    Nitrogen_Oxide = models.CharField(max_length=30,blank=False)
    Ozone = models.CharField(max_length=30,blank=False)
    Sulphur_Dioxide = models.CharField(max_length=30,blank=False) 
    Ambient_Temperature = models.CharField(max_length=30,blank=False)
    Particulate_Matter_10 = models.CharField(max_length=30,blank=False)
    Benzene = models.CharField(max_length=30,blank=False)
    Nitrogen_Dioxide = models.CharField(max_length=30,blank=False)
    Oxides_of_Nitrogen = models.CharField(max_length=30,blank=False)
    p_Xylene = models.CharField(max_length=30,blank=False)
    Toluene = models.CharField(max_length=30,blank=False)
    Barometric_Pressure = models.CharField(max_length=30,blank=False)
    Particulate_Matter_2 = models.CharField(max_length=30,blank=False) 
    Solar_Radiation = models.CharField(max_length=30,blank=False)

    def __str__(self):
        return str(self.Station_Name)    
        



