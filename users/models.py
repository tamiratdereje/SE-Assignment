from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models import fields
from django.db.models.deletion import CASCADE, SET_NULL
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth import get_user_model
from django.urls import reverse

from tech_cust_project.settings import AUTH_USER_MODEL

# Create your models here.
class User(AbstractUser):
    is_customer = models.BooleanField(default=False)
    is_technician = models.BooleanField(default=False)
    
class Device(models.Model):
    deviceId = fields.CharField(max_length=30)
    deviceName = fields.CharField(max_length=30)
    deviceDescription = models.CharField(max_length=50)
    ProfilePicture = models.ImageField(
                            upload_to='images/', 
                            height_field=None, 
                            width_field=None, 
                            max_length=None)
    def __str__(self):
        return self.deviceName  


class Location(models.Model):
    locationId = fields.CharField(max_length=30)
    locationName = fields.CharField(max_length=30)
    def __str__(self):
        return self.locationName  

class Technician(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    FullName = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    location = models.ForeignKey(Location,on_delete=CASCADE,null=False,default=1)
    organization = models.CharField(max_length=20, blank=True, null=True)
    profile_pic = models.ImageField(default="logo of profile.png", null=True, blank=True)    
    isApproved = models.BooleanField(default=False)
    phoneNumber = PhoneNumberField(blank=True)
    # rating = models.IntegerField(default = 0)
    device = models.ForeignKey(Device,on_delete=CASCADE,null=False,default=1)
    def __str__(self):
        return self.user.username

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    FullName = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True) 
    phoneNumber = PhoneNumberField(blank=True)
    profile_pic = models.ImageField(default="logo of profile.png", null=True, blank=True)    
    location = models.ForeignKey(Location,on_delete=CASCADE,null=False,default=1)

    def __str__(self):
        return self.user.username

class Order(models.Model):
    user = models.ForeignKey(AUTH_USER_MODEL, on_delete= models.SET_NULL, null=True,blank=True)
    technician = models.ForeignKey(Technician, on_delete= models.SET_NULL, null=True,blank=True)
    device = models.ForeignKey(Device,on_delete=CASCADE,null=False,default=1)
    STATUS = (("accepted","accepted" ),
                ("pending","pending"),
                ("done","done"),
            )
    status = models.CharField(max_length=200, null=True, choices=STATUS)
    date = models.DateTimeField(auto_now_add=True, null=True)

    def get_absolute_url(self):
        return f'/users/selectedTechnicianList/{self.device_id}'

class Feedback(models.Model):
    user = models.ForeignKey(AUTH_USER_MODEL, on_delete= models.SET_NULL, null=True,blank=True)
    email = models.EmailField(blank=False)
    name = models.CharField(max_length=300)
    company = models.CharField(max_length=300)
    subject = models.CharField(max_length=300)
    date = models.DateTimeField(auto_now_add=True, null=True)
    messages = models.TextField(max_length=300)


class Payment(models.Model):
    user = models.ForeignKey(AUTH_USER_MODEL, on_delete= models.SET_NULL, null=True,blank=True)
    content = models.CharField(max_length=300)
    price = models.CharField(max_length=300)
    AccountInforamtion = models.CharField(max_length=300)
    