from os import name
from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import reverse

# Create your models here.
class User(AbstractUser):
    is_customer = models.BooleanField(default=False)
    is_technician = models.BooleanField(default=False)
 
class Device(models.Model):
        device_choice = (
        ('Television','Television'),
        ('Fridge','Fridge'),
        ('Printer','Printer'),
        ('Phone','Phone'),
        ('Oven','Oven'),
        ('Laptop','Laptop'),
    )
        device = models.CharField(max_length=20, choices=device_choice)
        def __str__(self):
            return self.name


class Location(models.Model):
    location_choice = (
        ('Addis Ketema','Addis Ketema'),
        ('Akakiya Kaliti','Akakiya Kaliti'),
        ('Arada','Arada'),
        ('Bole','Bole'),
        ('Gullele','Gullele'),
        ('Kirkos','Kirkos'),
        ('Kofle Keranio','Kofle Keranio'),
        ('Lideta','Lideta'),
        ('Nifas Silk-Lafto','Nifas Silk-Lafto'),
        ('Yeka','Yeka'),
    )
    location = models.CharField(max_length=20, choices=location_choice)


class Technician(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    location = models.OneToOneField(Location, on_delete=models.CASCADE)
    organization = models.CharField(max_length=20, blank=True, null=True)
    profile_picture = models.ImageField(default='default_profile_picture.jpg', upload_to='profile_picture')
    isApproved = models.BooleanField(default=False)
    device = models.OneToOneField(Device, on_delete=models.CASCADE)
    def __str__(self):
        return self.user.username
 

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True) 
    phoneNumber = PhoneNumberField(blank=True)
    location = models.OneToOneField(Location, on_delete=models.CASCADE)
    def __str__(self):
        return self.user.username

