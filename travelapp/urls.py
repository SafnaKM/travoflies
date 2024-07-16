from . import views
from django.urls import path
urlpatterns=[
    path('',views.home,name='home'),
    path('about/',views.about,name='about'),
    path('services/',views.service,name='services'),
    path('destination/',views.place,name='destination'),
    path('contact/',views.contact,name='contact'),
    path('enquiry/',views.enquiry,name='enquiry'),
   
]