from django import forms
from phonenumber_field.formfields import PhoneNumberField
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.db import models
from django.db import transaction

from .models import Device, Location, User, Customer, Technician



class CustomerSignUpForm(UserCreationForm):
    location = forms.ChoiceField(choices=Location.location_choice)
    phoneNumber = PhoneNumberField()

    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_customer = True
        user.save()
        customer = Customer.objects.create(user=user)
        customer.location.add(*self.cleaned_data.get('location'))
        customer.phoneNumber.add(*self.cleaned_data.get('phoneNumber'))
        return user



class TechnicianSignUpForm(UserCreationForm):
    device = forms.ChoiceField(choices=Device.device_choice)
    organization = forms.CharField(help_text="optional")
    profile_picture = forms.ImageField()
    location = forms.ChoiceField(choices=Location.location_choice)


    
    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_technician = True
        if commit:
            user.save()
        technician = Technician.objects.create(user=user)
        technician.location.add(*self.cleaned_data.get('location'))
        technician.organization.add(*self.cleaned_data.get('organization'))
        technician.profile_picture.add(*self.cleaned_data.get('profile_picture'))
        technician.device.add(*self.cleaned_data.get('device'))

        return user


