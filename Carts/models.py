from CustomizedUserModel.models import Userperson
from Products.models import ProductSubCategories_1
from Sellers.models import Sellers
from django.db import models

class Carts(models.Model):
    shoper = models.ForeignKey(Userperson,on_delete=models.CASCADE,verbose_name='Shoper')
    payment_date = models.DateTimeField(auto_created=True,verbose_name='Payment Date')
    payment_status = models.BooleanField(default=True,verbose_name='Payment Status')
    
    def __str__(self):
        return f'{self.shoper}'
    

class Orders(models.Model):
    cart = models.ForeignKey(Carts,on_delete=models.CASCADE,verbose_name='Cart')
    title = models.CharField(max_length=999,blank=True,null=True,verbose_name='Title')
    description = models.TextField(verbose_name='Description')
    price = models.IntegerField(blank=True,null=True,verbose_name='Price')
    discounted_price = models.IntegerField(blank=True,null=True,verbose_name='Discounted Price')
    seller = models.ForeignKey(Sellers,on_delete=models.CASCADE,verbose_name='Seller')
    category = models.ManyToManyField(ProductSubCategories_1,verbose_name='Category')
    score = models.IntegerField(default=1,verbose_name='Score')
    payment_date = models.DateTimeField(auto_created=True,verbose_name='Payment Date')
    payment_status = models.BooleanField(default=True,verbose_name='Payment Status')
    
    def __str__(self):
        return f'{self.title}'