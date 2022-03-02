from pyexpat import model
from tabnanny import verbose
from CustomizedUserModel.models import Userperson
from Sellers.models import Sellers
from django.db import models

# Products category model
class ProductCategories(models.Model):
    name = models.CharField(max_length=999,verbose_name='Name')
    status = models.BooleanField(default=False,verbose_name='Status')
    
    def __str__(self):
        return f'{self.name}'

# Products models
class Products(models.Model):
    title = models.CharField(max_length=999,blank=True,null=True,verbose_name='Title')
    slug = models.SlugField(max_length=999)
    description = models.TextField(verbose_name='Description')
    price = models.IntegerField(blank=True,null=True,verbose_name='Price')
    discounted_price = models.IntegerField(blank=True,null=True,verbose_name='Discounted Price')
    seller = models.ForeignKey(Sellers,on_delete=models.CASCADE,verbose_name='Seller')
    category = models.ManyToManyField(ProductCategories,verbose_name='Category')
    score = models.IntegerField(default=1,verbose_name='Score')
    date = models.DateTimeField(auto_now_add=True,blank=True,null=True,verbose_name='Date')
    inventory = models.IntegerField(blank=False,verbose_name='Inventory')
    
    def __str__(self):
        return f'{self.title}'

class ProductsComments(models.Model):
    user = models.ForeignKey(Userperson,on_delete=models.CASCADE,verbose_name='User')
    status = models.BooleanField(default=False,verbose_name='Status')
    comment = models.TextField(verbose_name='Comment')
    product = models.ForeignKey(Products, on_delete=models.CASCADE, null=False, blank=False ,verbose_name='Prodcut Id') # to be fxed
    
    def __str__(self):
        return f'{self.user}'

class TrackingCode(models.Model):
    status_choice = [
        ('confirming','در حال تایید'),
        ('confirmed', 'تایید شده'),
        ('sending', 'در حال ارسال'),
        ('processed', 'اتمام')
    ]
    product = models.ForeignKey(Products, on_delete=models.CASCADE, verbose_name='Product')
    tracking_code = models.CharField(max_length=150, blank=False, verbose_name='Tracking Code')
    code_status = models.BooleanField(verbose_name='Code Status')
    product_status = models.CharField(choices=status_choice, blank=False, verbose_name = 'Product_status', max_length=100)

    def __str__(self):
        return f'{self.tracking_code}'
    
class Color(models.Model):
    name = models.CharField(max_length=150, blank=False)
    color_code = models.CharField(max_length=300)

    def __str__(self):
        return f'{self.name}'
    
class Scores(models.Model):
    product = models.ForeignKey(Products, on_delete=models.CASCADE, verbose_name='Prodcut ID', related_name='product')
    total_score = models.IntegerField(blank=False,verbose_name='"Total Score')

    def __str__(self):
        return f'{self.total_score}'

