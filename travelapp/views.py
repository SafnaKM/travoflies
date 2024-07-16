from django.shortcuts import render,redirect
from .models import Package
from .models import Destination
from .models import Person
from .models import Enquiry
from .forms import EnquiryForm
from django.contrib import messages


# Create your views here.
def home(request):
    package_obj= Package.objects.all()
    dest_obj=Destination.objects.all()
    person_detail=Person.objects.all()
    return render(request,'index.html',{'result_pkg':package_obj,'result_dest':dest_obj,'res_review':person_detail})
def about(request):
    package_obj= Package.objects.all()
    dest_obj=Destination.objects.all()
    person_detail=Person.objects.all()
    return render(request,'about.html',{'result_pkg':package_obj,'result_dest':dest_obj,'res_review':person_detail})
def service(request):
     package_obj= Package.objects.all()
     dest_obj=Destination.objects.all()
     person_detail=Person.objects.all()
     return render(request,'service.html',{'result_pkg':package_obj,'result_dest':dest_obj,'res_review':person_detail})
def place(request):
    package_obj= Package.objects.all()
    dest_obj=Destination.objects.all()
    person_detail=Person.objects.all()
    return render(request,'package.html',{'result_pkg':package_obj,'result_dest':dest_obj,'res_review':person_detail})


def contact(request):
     return render(request,'footer.html')
def enquiry(request):
    if request.method == 'POST':
        form = EnquiryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your enquiry has been submitted successfully!')
            return redirect('enquiry') 
        
    else:
        form = EnquiryForm()
    
    return render(request, 'enquiry.html', {'form': form})