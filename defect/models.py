from django.db import models
from django.urls import reverse
from django_jalali.db import models as jmodels
from django.dispatch import receiver
from django.db.models.signals import pre_save
from datetime import time,date,datetime,timedelta





class Station(models.Model):
    name=models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("stations")
    


class Fault(models.Model):
    name=models.CharField(max_length=100)
    file=models.FileField(null=True,blank=True)
    
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse("faults")
    

class Report(models.Model):
    fault=models.ForeignKey('Fault',blank=True,on_delete=models.SET_NULL,null=True)
    station=models.ForeignKey('Station',on_delete=models.SET_NULL,null=True,blank=False)
    description=models.TextField(null=True,blank=True)
    shift=models.CharField(max_length=1 ,choices=[('A','A'),('B','B'),('C','C')],null=True,blank=True)
    reporter=models.CharField(max_length=100, null=True,blank=True)
    expert=models.CharField(max_length=100,null=True,blank=True)
    opinion=models.TextField(null=True ,blank=True)
    piece=models.ManyToManyField('Piece' , null=True ,blank=True)
    date=jmodels.jDateField()
    startTime=models.TimeField()
    endTime=models.TimeField()
    stopTime=models.TimeField(blank=True)

    def __str__(self):
        return str(self.fault) +" "+str(self.station)



@receiver(pre_save,sender=Report)
def calcStopTime(sender ,instance,**kwargs):
    end=str(instance.endTime).split(':')
    start=str(instance.startTime).split(':')
    instance.stopTime=str(timedelta(hours=int(end[0]),minutes=int(end[1]),seconds=int(end[2]))-timedelta(hours=int(start[0]),minutes=int(start[1]),seconds=int(start[2])))





class Piece (models.Model):
    name=models.CharField(max_length=100)
    ikco_id=models.CharField(max_length=100)
    technical_id=models.CharField(max_length=100)


    def __str__(self):
        return self.name