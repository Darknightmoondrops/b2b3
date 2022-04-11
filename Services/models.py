from extensions.optimization import photo_optimization
from CustomizedUserModel.models import Userperson
from extensions.DateJalali import django_jalali
from django.db import models


# Service categoies model
class ServiceCategories(models.Model):
    name = models.CharField(max_length=999,verbose_name='Name')
    status = models.BooleanField(default=False,verbose_name='Status')
    
    def __str__(self):
        return f'{self.name}'
    
# Service model
class Services(models.Model):
    service_user = models.ForeignKey(Userperson,on_delete=models.CASCADE,verbose_name='service user')
    title = models.CharField(max_length=999,blank=True,null=True,verbose_name='Title service')
    image = models.ImageField(upload_to='Services',blank=True,null=True,verbose_name='Image')
    description = models.TextField(blank=True,null=True,verbose_name='Description')
    short_description = models.TextField(blank=True,null=True,verbose_name='Description')
    categories = models.ManyToManyField(ServiceCategories,verbose_name='Categories')
    score = models.IntegerField(default=1,blank=True,null=True,verbose_name='Score')
    date = models.DateTimeField(auto_now_add=True, verbose_name='Date')

    def save(self, *args, **kwargs):
        super(Services, self).save(*args, **kwargs)
        if self.image:
            photo_optimization(self.image)
            super(Services, self).save(*args, **kwargs)

    def jdate(self):
        return django_jalali(self.date)
    
    def __str__(self):
        return f'{self.title}'


class ServicesComments(models.Model):
    user = models.ForeignKey(Userperson,on_delete=models.CASCADE,verbose_name='User')
    status = models.BooleanField(default=False,verbose_name='Status')
    service_image = models.ImageField(upload_to='ProductsCommentsImage',blank=True,null=True,verbose_name='Image')
    service_title = models.TextField(blank=True,null=True,verbose_name='Title')
    service_short_description = models.TextField(blank=True,null=True,verbose_name='Short description')
    comment = models.TextField(verbose_name='Comment')
    services = models.ForeignKey(Services, on_delete=models.CASCADE, null=False,blank=False,verbose_name='Services Id')
    date = models.DateTimeField(auto_now_add=True, blank=True, null=True, verbose_name='Date')

    def save(self, *args, **kwargs):
        super(ServicesComments, self).save(*args, **kwargs)
        if self.service_image:
            photo_optimization(self.service_image)
            super(ServicesComments, self).save(*args, **kwargs)

    def jdate(self):
        return django_jalali(self.date)


    def __str__(self):
        return f'{self.user}'