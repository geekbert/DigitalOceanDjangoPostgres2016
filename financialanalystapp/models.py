from django.db import models

# Create your models here.

import datetime
from django.utils import timezone

from decimal import *
import operator

class Company(models.Model):
    Year = models.CharField(max_length=4)
    Quarter = models.CharField(max_length=1, blank=True)
    Date = models.DateField('Date')
    Company = models.CharField(max_length=50, blank=True)
    Revenues = models.DecimalField(max_digits=19, decimal_places=2, blank = True)
    CostofSales = models.DecimalField(max_digits=19, decimal_places=2, blank=True)
    SGandA = models.DecimalField(max_digits=19, decimal_places=2, blank = True)
    EBIT = models.DecimalField(max_digits=19, decimal_places=2, blank = True)
    def get_Operating_Margin(self): 
        getcontext().prec = 3
        return self.EBIT/self.Revenues
    OperatingMargin = property(get_Operating_Margin)
    Employees = models.PositiveIntegerField(default = 0)
    # test for charField
    PPE = models.CharField(max_length=15, blank = True)
    def get_EBITperEmployee(self):
        getcontext().prec = 3
        return (self.EBIT/self.Employees)*1000000
    def divide(self,x,y): 
        getcontext().prec = 3
        return round(self.x/self.y, 3)
    def get_RevenueperEmployee(self):
        return (self.Revenues/self.Employees)*1000000
    def get_PPEperEmployee(self): 
        return round((float(self.PPE)/self.Employees)*1000000)
    RevenueperEmployee = property(get_RevenueperEmployee)
    EBITperEmployee = property(get_EBITperEmployee)
    PPEperEmployee = property(get_PPEperEmployee)
    linktoAR = models.URLField(blank=True)
    Comment = models.CharField(max_length=400, blank=True)
    active = models.BooleanField(default=True)

    def __str__(self):              # __unicode__ on Python 2
        return self.Year
    def __str__(self):              # __unicode__ on Python 2
        return self.Quarter
    def __str__(self):              # __unicode__ on Python 2
        return self.Date
    def __str__(self):              # __unicode__ on Python 2
        return self.Customer    
    def __str__(self):              # __unicode__ on Python 2
        return self.Comment
    
    def was_published_recently(self):
        return self.Date >= timezone.now() - datetime.timedelta(days=1)	
    
