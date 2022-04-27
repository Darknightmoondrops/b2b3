from extensions.optimization import photo_optimization
from extensions.DateJalali import django_jalali
from CustomizedUserModel.models import Userperson
from django.db import models


# Vendor Categories model
class VendorCategories(models.Model):
    name = models.CharField(max_length=999,verbose_name='Name')
    status = models.BooleanField(default=False,verbose_name='Status')

    def __str__(self):
        return f'{self.name}'
        

# Sellers model
class Sellers(models.Model):
    business_owner = models.ForeignKey(Userperson,on_delete=models.CASCADE,verbose_name='Business Owner')
    business_name = models.CharField(max_length=999,verbose_name='Business Name')
    business_description = models.TextField(verbose_name='Business Description')
    business_image = models.ImageField(upload_to='Businessimage',blank=True,null=True,verbose_name='Business Image')
    business_license = models.ImageField(upload_to='BusinessLicenseImage',blank=True,null=True,verbose_name='Business License')
    registration_date = models.DateTimeField(auto_now_add=True,verbose_name='Registration Date')
    business_status = models.BooleanField(default=False,verbose_name='business Status')
    business_categories = models.ManyToManyField(VendorCategories,verbose_name='business Categories')

    def save(self, *args, **kwargs):
        photo_optimization(self.business_image)
        photo_optimization(self.business_license)
        super(Sellers, self).save(*args, **kwargs)


    def business_owner_info(self):
        return self.business_owner.fullname

    def business_categories_info(self):
        return [{category.id:category.name} for category in self.business_categories.all()]

    def jdate(self):
        return django_jalali(self.registration_date)

    def __str__(self):
        return f'{self.business_name}'
        