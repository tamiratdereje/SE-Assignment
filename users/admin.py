from django.contrib import admin
from users.models import User, Customer, Technician, Location, Device, Order,Feedback,Payment

# Register your models here.0
admin.site.register(User)
admin.site.register(Customer)
admin.site.register(Technician)
admin.site.register(Location)
admin.site.register(Device)
admin.site.register(Order)
admin.site.register(Feedback)
admin.site.register(Payment)



