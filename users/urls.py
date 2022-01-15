
from django.urls import path
from .views import FeedbackCreateView, homePageView
from .views import CustomerSignUpView,TechnicianSignUpView, SignUpView, TechnicianAccountSetting, CustomerAccountSetting, OrderCreateView,PaymentCreateView,TechnicianListView,SelectedTechnicianView,AboutView,SeeOrderView
from .views import PasswordsChangeView, PasswordsResetView


urlpatterns = [
    path('', homePageView, name='home'),
    path('about/', AboutView, name="about"),
    path('SeeOrder/', SeeOrderView.as_view(), name="order"),

    # path('orderTechnicianList/', techOrderView.as_view(), name="ordertechlist"),
    path('selectedTechnicianList/<int:pk>', SelectedTechnicianView.as_view(), name="selectedtechlist"),
    path('technicianList/', TechnicianListView.as_view(), name="techlist"),
    path('makepayment/', PaymentCreateView.as_view(), name="makepayment"),
    path('order/', OrderCreateView.as_view(), name="orderit"),
    path('feedback/', FeedbackCreateView.as_view(), name="feeditback"),
    path('technician_account_setting/', TechnicianAccountSetting, name="technician_account_setting"),
    path('customer_account_setting/', CustomerAccountSetting, name="customer_account_setting"),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('signup/Customer/', CustomerSignUpView.as_view(), name='customer_signup'),
    path('signup/Technician/', TechnicianSignUpView.as_view(), name='technician_signup'),
    path('/passwordChange', PasswordsChangeView.as_view(template_name='registration/password_change.html'), name='change password'),
    path('/passwordReset', PasswordsResetView.as_view(template_name='registration/password_reset_form.html'), name='forgot password'),


]
