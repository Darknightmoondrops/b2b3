from CustomizedUserModel.models import Userperson
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
    date = models.DateTimeField(auto_now_add=True,verbose_name='Date')
    categories = models.ManyToManyField(ServiceCategories,verbose_name='Categories')
    
    def __str__(self):
        return f'{self.service_user}'