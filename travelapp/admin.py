# admin.py
from django.contrib import admin
from .models import Destination, Package, Person, Enquiry

# Register your models here.
admin.site.site_header = 'Travofly'
admin.site.register(Destination)
admin.site.register(Person)
admin.site.register(Package)

class EnquiryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'contact_number', 'dest_name', 'your_country', 'no_of_days', 'no_of_adults', 'no_of_children', 'message', 'submitted_at')

admin.site.register(Enquiry, EnquiryAdmin)
