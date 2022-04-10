from CustomizedUserModel.models import Userperson
from django.db import models

class Codes(models.Model):
    user = models.ForeignKey(Userperson,on_delete=models.CASCADE,verbose_name='User')
    status = models.BooleanField(default=False,blank=True,null=True,verbose_name='Status')
    code = models.IntegerField(blank=True,null=True,verbose_name='Code')

    def __str__(self):
        return f'{self.code}'
