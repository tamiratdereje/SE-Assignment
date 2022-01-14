# from typing_extensions import Required
from django import forms
from django.db.models.fields import CharField, EmailField
from phonenumber_field.formfields import PhoneNumberField
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.db import models
from django.db import transaction
from django.forms import ModelForm


from .models import Device, Feedback, Location, User, Customer, Technician,Feedback

# Order,


class CustomerSignUpForm(UserCreationForm):
    FullName = forms.CharField()
    email = forms.EmailField()
    phoneNumber = PhoneNumberField()
    location = forms.ModelChoiceField(Location.objects.all())
    
    class Meta(UserCreationForm.Meta):
        model = User


    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_customer = True
        user.save()
        customer = Customer.objects.create(user=user)
        customer.email = self.cleaned_data.get('email')
        customer.FullName = self.cleaned_data.get('FullName')
        customer.location = self.cleaned_data.get('location')
        customer.phoneNumber = self.cleaned_data.get('phoneNumber')
        customer.save()
        return user


class TechnicianSignUpForm(UserCreationForm):

    FullName = forms.CharField()
    email = forms.EmailField()
    phoneNumber = PhoneNumberField()
    location = forms.ModelChoiceField(Location.objects.all())
    device = forms.ModelChoiceField(Device.objects.all())
    organization = forms.CharField(help_text="optional")
    # profile_pic = forms.ImageField()
   
    class Meta(UserCreationForm.Meta):
        model = User
        

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_technician = True
        user.save()
        technician = Technician.objects.create(user=user)
        technician.FullName = self.cleaned_data.get('FullName')
        technician.email = self.cleaned_data.get('email')
        technician.location = self.cleaned_data.get('location')
        technician.organization = self.cleaned_data.get('organization')
        technician.phoneNumber = self.cleaned_data.get('phoneNumber')
        # technician.profile_pic = self.cleaned_data.get('profile_pic')
        technician.device = self.cleaned_data.get('device')
        technician.save()

        return user

class CustomerAccountForm(ModelForm):
	class Meta:
		model = Customer
		fields = '__all__'
		exclude = ['user']

class TechnicianAccountForm(ModelForm):
	class Meta:
		model = Technician
		fields = '__all__'
		exclude = ['user'], 'isApproved','user'
        


# class OrderForm(ModelForm):
#     class Meta:
#         model = Order
#         fields = '__all__'
        # exclude = 'status','date'

		

# class FeedbackForm(ModelForm):
# 	class Meta:
# 		model = Feedback
# 		fields = '__all__'