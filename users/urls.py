
from django.urls import path
from .views import homePageView
# from .views import SignUpView, CustomerSignUpView, TechnicianSignUpView
from django.views.generic.base import TemplateView # new
from .views import CustomerSignUpView,TechnicianSignUpView, SignUpView

urlpatterns = [
    path('', homePageView, name='home'),
    # path('', TemplateView.as_view(template_name='home.html'),name='home'), 
    path('users/signup/', SignUpView.as_view(), name='signup'),
    path('users/signup/Customer/', CustomerSignUpView.as_view(), name='customer_signup'),
    path('users/signup/Technician/', TechnicianSignUpView.as_view(), name='technician_signup'),

]
