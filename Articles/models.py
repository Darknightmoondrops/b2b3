from CustomizedUserModel.models import Userperson
from django.db import models

class Articles(models.Model):
    title = models.CharField(max_length=999,verbose_name='Title')
    writer = models.ForeignKey(Userperson,on_delete=models.CASCADE,blank=True,null=True,verbose_name='Writer')
    date = models.DateField(auto_now_add=True,verbose_name='Date')
    keywords = models.TextField(verbose_name='Keywords')
    description = models.TextField(verbose_name='Description', default='a short description')
    
    def __str__(self):
        return f'{self.title}'