
from django.db import models
from django.core.validators import MinValueValidator


# Create your models here.
class Destination(models.Model):
    img=models.ImageField(upload_to='pics')
    other_img=models.ImageField(upload_to='pics')
    dest_name = models.CharField(max_length=250)
    location=models.CharField(max_length=250)
    def __str__(self):
        return self.dest_name

class Package(models.Model):
    img=models.ImageField(upload_to='pics')
    pkg_name=models.CharField(max_length=250)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    days=models.IntegerField(validators=[MinValueValidator(0)])
    usernum=models.IntegerField( validators=[MinValueValidator(0)])
    location=models.CharField(max_length=250)
    def __str__(self):
        return self.pkg_name

class Person(models.Model):
     name=models.CharField(max_length=250)
     img=models.ImageField(upload_to='pics')
     desc=models.TextField()
     def __str__(self):
        return self.name
     
class Enquiry(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    contact_number = models.CharField(max_length=20)
    dest_name = models.ForeignKey(Destination, on_delete=models.CASCADE)
    your_country = models.CharField(max_length=255)
    no_of_days = models.IntegerField()
    no_of_adults = models.IntegerField()
    no_of_children = models.IntegerField()
    message = models.TextField(blank=True, null=True)
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name