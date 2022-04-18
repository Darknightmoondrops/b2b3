from extensions.optimization import photo_optimization
from CustomizedUserModel.models import Userperson
from extensions.DateJalali import django_jalali
from django.db import models
import datetime


# Service categoies model
class ServicesTypeOfCleaningSpace(models.Model):
    name = models.CharField(max_length=999,verbose_name='Name')
    status = models.BooleanField(default=False,verbose_name='Status')
    
    def __str__(self):
        return f'{self.name}'

# Service model
class Services(models.Model):
    service_user = models.ForeignKey(Userperson,on_delete=models.CASCADE,verbose_name='service user')
    title = models.CharField(max_length=999,blank=True,null=True,verbose_name='Title service')
    company = models.CharField(max_length=999,blank=True,null=True,verbose_name='Company')
    image = models.ImageField(upload_to='Services',blank=True,null=True,verbose_name='Image')
    description = models.TextField(blank=True,null=True,verbose_name='Description')
    short_description = models.TextField(blank=True,null=True,verbose_name='Description')
    type_of_cleaning_space = models.ManyToManyField(ServicesTypeOfCleaningSpace,verbose_name='Categories')
    score = models.IntegerField(default=1,blank=True,null=True,verbose_name='Score')
    date = models.DateTimeField(auto_now_add=True, verbose_name='Date')

    def save(self, *args, **kwargs):
        super(Services, self).save(*args, **kwargs)
        if self.image:
            photo_optimization(self.image)
            super(Services, self).save(*args, **kwargs)

    def service_user_fullname(self):
        return self.service_user.fullname

    def service_user_gender(self):
        return self.service_user.gender

    def service_reservations(self):
        reservations = ServicesReservation.objects.filter(service_user_id=self.id).all()
        return [{r.hour: r.status} for r in reservations]

    def jdate(self):
        return django_jalali(self.date)

    def __str__(self):
        return f'{self.title}'




class ServicesReservation(models.Model):
    service_user = models.ForeignKey(Services,on_delete=models.CASCADE,verbose_name='Service User',related_name='service_reservation')
    hour = models.CharField(max_length=999,blank=True,null=True,verbose_name='Hours')
    status = models.BooleanField(default=False,verbose_name='Status')


    # def save(self, *args, **kwargs):
    #     date_now = str(datetime.datetime.now()).split(' ')
    #     date_hour = str(date_now[1]).split('.')
    #     hour_split = str(date_hour[0]).split(':')
    #     hour = f'{hour_split[0]}:{hour_split[1]}'
    #     self.hour = hour
    #     super(ServicesReservation, self).save(*args, **kwargs)


    def __str__(self):
        return f'{self.hour}'



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