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




