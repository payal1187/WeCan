from django.contrib import admin
from myApp1.models import *

# Register your models here.

# class Contact_Admin(admin.ModelAdmin):
#     list_display =  ['email']
    
    
# admin.site.register(Contact,Contact_Admin)
admin.site.register(ContactModel)
