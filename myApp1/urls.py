from myApp1.views import  index,about,contact_details,contact
from django.urls import path

urlpatterns = [
    path("",index,name='home'),
    path('contact/',contact, name='contact'),
    # path("contact_api/",ContactAPIView.as_view(),name='contact_api'),
    path("about/",about,name='about'),
    #path('dashboard/',Admin_panel,name='dashboard'),
    path('save_details/',contact_details,name='save_details')
   
]