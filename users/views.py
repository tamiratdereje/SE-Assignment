from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy

# from .forms import CustomUserCreationForm
from django.contrib.auth.views import PasswordChangeView
# Create your views here.
from .models import User
# from django.http import c
from .forms import CustomerSignUpForm, TechnicianSignUpForm

from django.contrib.auth import authenticate, login
from django.shortcuts import redirect
from django.views.generic import CreateView, TemplateView
from django.db import IntegrityError



def homePageView(request):
    return render(request, "home.html")

class SignUpView(TemplateView):
    template_name = 'signup.html'


class CustomerSignUpView(CreateView):
    model = User
    form_class = CustomerSignUpForm
    template_name = 'customer_signup.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'customer'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        try:
            user = form.save()
    # code that produces error
        except IntegrityError as e:
            return redirect('home')
        
        login(self.request, user)
        return redirect('home')


class TechnicianSignUpView(CreateView):
    model = User
    form_class = TechnicianSignUpForm
    template_name = 'technician_signup.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'technician'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')

 

