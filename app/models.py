from django.db import models

# Create your models here.


class siteedit(models.Model):
    name = models.CharField( max_length=50 ,blank=True, null=True,)
    email = models.CharField( max_length=50 ,blank=True, null=True,)
    domain = models.CharField( max_length=50 ,default=name, blank=True, null=True,)
    Address = models.CharField( max_length=50 ,blank=True, null=True,)
    country = models.CharField( max_length=50 ,blank=True, null=True,)
    dis = models.TextField( blank=True, null=True,)
    phone = models.CharField( max_length=50 ,blank=True, null=True,)
    logo = models.TextField( blank=True, null=True,)
    image1 = models.TextField( blank=True, null=True,)
    idx = models.IntegerField( default=1) 
    

   
    def __str__(self):
        return self.name
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    from django.db import models
from .genUid import *
import datetime
# Create your models here.


class shippment(models.Model):
    SName =models.CharField( max_length=50,blank=True , null=True,)
    SAddress =models.TextField( blank=True , null=True,)
    SEmail =models.CharField( max_length=50,blank=True , null=True,)
    SPhone =models.CharField( max_length=50,blank=True , null=True,)
    message =  models.TextField(blank=True , null=True,)
    RName =models.CharField( max_length=50,blank=True , null=True,)
    RAddress =models.TextField( blank=True , null=True,)
    REmail =models.CharField( max_length=50,blank=True , null=True,)
    RPhone =models.CharField( max_length=50,blank=True , null=True,)
    Origin =models.CharField( max_length=50,blank=True , null=True,)
    Destination =models.CharField( max_length=50,blank=True , null=True,)
    Mode =models.CharField( max_length=50,blank=True , null=True,)
    uuid =models.CharField( max_length=50,blank=True , null=True, default=genUdis(12))
    Quantity =models.CharField( max_length=50,blank=True , null=True,)
    Weight  =models.CharField( max_length=50,blank=True , null=True,)
    Amount   =models.CharField( max_length=50,blank=True , null=True,)
    PaymentMode   =models.CharField( max_length=50,blank=True , null=True,)
    Delivery   =models.CharField( max_length=50,blank=True , null=True,)
    DepartureDate   =models.CharField( max_length=50,blank=True , null=True,)
    PackageItems   =models.TextField( blank=True , null=True,)
    message =  models.TextField(blank=True , null=True,)
    datetimec = models.DateTimeField( auto_now_add=True,blank=True , null=True,)
    datetimecmain = models.DateTimeField( blank=True , null=True,)
    history = models.ManyToManyField('shippmenthistory',blank=True) 
    def __str__(self):
        return f'the userid {self.id}'
class shippmenthistory(models.Model):
    Location =models.CharField( max_length=50,blank=True , null=True,)
    Status =models.CharField( max_length=50,blank=True , null=True)
    datetimec = models.CharField( max_length=50,blank=True , null=True,)
    Remarks =models.CharField( max_length=50,blank=True , null=True,)
    def __str__(self):
        return f'the userid {self.id}'