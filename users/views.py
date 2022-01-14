from pyexpat import model
from urllib import request
from django.db.models import fields
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
from django.urls import reverse_lazy

from django.contrib.auth.views import PasswordChangeView,PasswordChangeDoneView, PasswordResetView
from django.contrib.auth.forms import PasswordChangeForm, PasswordResetForm
# Create your views here.
from .models import Customer, Feedback, Payment, Technician, User, Order
from .forms import CustomerSignUpForm, TechnicianSignUpForm, CustomerAccountForm, TechnicianAccountForm,CustomerAccountForm

from django.contrib.auth import authenticate, login
from django.shortcuts import redirect
from django.views.generic import CreateView, TemplateView
from django.views.generic import ListView

from users import models
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
        user = form.save()
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



class PasswordsChangeView(PasswordChangeView):
    form_class = PasswordChangeForm
    # reverse_lazy('singup')

class PasswordsResetView(PasswordResetView):
    form_class = PasswordResetForm
    

def TechnicianAccountSetting(request):
	technician = request.user.technician
	form = TechnicianAccountForm(instance=technician)

	if request.method == 'POST':
		form = TechnicianAccountForm(request.POST, request.FILES,instance=technician)
		if form.is_valid():
			form.save()


	context = {'form':form}
	return render(request, 'technician_account_setting.html', context)



def CustomerAccountSetting(request):
	customer = request.user.customer
	form = CustomerAccountForm(instance=customer)

	if request.method == 'POST':
		form = CustomerAccountForm(request.POST, request.FILES,instance=customer)
		if form.is_valid():
			form.save()


	context = {'form':form}
	return render(request, 'customer_account_setting.html', context)


class OrderCreateView(LoginRequiredMixin,CreateView):
    model = Order
    template_name = 'orderpage.html'
    fields = ('device',)
    # fields = ('title', 'body')
    # global success_url
    # def save(self, request):
    #     temp = request.POST.get("device")
    #     super.save()
        # global success_url
        # success_url = f'/users/selectedTechnicianList/{temp}'
    # form_class = OrderForm
    login_url = 'login'
    order_device = None
    # def save(self, request):
    #     super.save()
    #     return request.order.device
    # success_url = '/order/{request.POST.get("device")}'

    def form_valid(self, form):
        form.instance.user = self.request.user
        
        return super().form_valid(form)
    

class FeedbackCreateView(CreateView):
    model = Feedback
    template_name = 'contact.html'
    fields =('email','name','company','subject','messages')

    success_url = '/'
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)



class PaymentCreateView(CreateView):
    model = Payment
    template_name = 'makepayment.html'
    # form_class = FeedbackForm
    fields = ('content','price','AccountInforamtion')

    success_url = '/'
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)



class TechnicianListView(LoginRequiredMixin, ListView):
    model = Technician
    template_name = 'technicians_list.html'
    login_url = 'login'
    queryset =  Technician.objects.all()
    

class SelectedTechnicianView(ListView):
    # model = Order
    # deviceName = Order.device
    # ordevice_id = Order.objects.get()

    model = Technician  
    template_name = 'selected_technicians_list.html'
    def get_queryset(self):
        # ordered = self.request.GET.get('pk')
        path = (self.request.path)
        path_list = path.split('/')
        last = int(path_list[-1])
        print(last)
        customer = self.request.user.customer
        customer_location = customer.location_id
        # query =  Technician.objects.all()
        # print(query[0].device_id)
        queryset = Technician.objects.all().filter(device_id=last)
        print(queryset)
        return queryset
        

# class techOrderView(ListView):
#     model = Order  
#     template_name = 'order_technicians_list.html'
#     def get_queryset(self):
#         technician = self.request.user.technician
#         tech_id = technician.location_id
#         queryset = Order.objects.filter(order_id=tech_id)
#         return queryset
