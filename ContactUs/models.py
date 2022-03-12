from django.db import models

class ContactUs(models.Model):
    firstName = models.CharField(max_length=100, blank=False)
    lastName = models.CharField(max_length=100, blank=False)
    email = models.EmailField(max_length=100,blank=True,null=True)
    contact_number = models.CharField(max_length=15, blank = False)
    company_name = models.CharField(max_length=100)
    subject = models.CharField(max_length=99)
    message = models.TextField()
    status = models.BooleanField(default=False)