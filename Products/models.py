from extensions.optimization import photo_optimization
from CustomizedUserModel.models import Userperson
from extensions.DateJalali import django_jalali
from Sellers.models import Sellers
from django.db import models


class ProductSubCategories_2(models.Model):
    name = models.CharField(max_length=999, verbose_name='Name')
    status = models.BooleanField(default=False, verbose_name='Status')

    def __str__(self):
        return f'{self.name}'


class ProductSubCategories_1(models.Model):
    name = models.CharField(max_length=999, verbose_name='Name')
    status = models.BooleanField(default=False, verbose_name='Status')
    sub_categories2 = models.ManyToManyField(ProductSubCategories_2, blank=True, verbose_name='Sub Categories 2')
    def __str__(self):
        return f'{self.name}'


class ProductMainCategories(models.Model):
    name = models.CharField(max_length=999,verbose_name='Name')
    image = models.ImageField(upload_to='ProductMainCategoriesImage',blank=True,null=True,verbose_name='Image')
    status = models.BooleanField(default=False,verbose_name='Status')
    sub_categories1 = models.ManyToManyField(ProductSubCategories_1,blank=True,verbose_name='Sub Categories 1')
    
    def __str__(self):
        return f'{self.name}'


class ProductsColor(models.Model):
    name = models.CharField(max_length=150, blank=False)
    code = models.CharField(max_length=300)

    def __str__(self):
        return f'{self.name}'

class ProductsSizes(models.Model):
    name = models.CharField(max_length=150, blank=False,null=False)

    def __str__(self):
        return f'{self.name}'

class Products(models.Model):
    title = models.CharField(max_length=999,blank=False,null=False,verbose_name='Title')
    slug = models.TextField(blank=False,null=False)
    main_image = models.ImageField(upload_to='productsImage',blank=False,null=False,verbose_name='Image')
    image1 = models.ImageField(upload_to='productsImage',blank=False,null=False,verbose_name='Image1')
    image2 = models.ImageField(upload_to='productsImage',blank=False,null=False,verbose_name='Image2')
    image3 = models.ImageField(upload_to='productsImage',blank=False,null=False,verbose_name='Image3')
    image4 = models.ImageField(upload_to='productsImage',blank=False,null=False,verbose_name='Image4')
    description = models.TextField(blank=False,null=False,verbose_name='Description')
    short_description = models.TextField(blank=False,null=False,verbose_name='Short Description')
    price = models.IntegerField(blank=False,null=False,verbose_name='Price')
    discounted_price = models.IntegerField(blank=False,null=False,verbose_name='Discounted Price')
    seller = models.ForeignKey(Sellers,blank=False,null=False,on_delete=models.CASCADE,verbose_name='Seller')
    maincategories = models.ManyToManyField(ProductMainCategories,blank=False,verbose_name='Main Category')
    subCategories1 = models.ManyToManyField(ProductSubCategories_1,blank=False,verbose_name='Sub Category 1')
    subCategories2 = models.ManyToManyField(ProductSubCategories_2,blank=False,verbose_name='Sub Category 2')
    colors = models.ManyToManyField(ProductsColor,blank=False,verbose_name='Colors')
    sizes = models.ManyToManyField(ProductsSizes,blank=False,verbose_name='Sizes')
    score = models.IntegerField(default=1,verbose_name='Score')
    date = models.DateTimeField(auto_now_add=True,blank=True,null=True,verbose_name='Date')
    inventory = models.IntegerField(blank=False,null=False,verbose_name='Inventory')

    def save(self, *args, **kwargs):
        self.slug = str(self.slug).replace(' ','-')
        photo_optimization(self.main_image)
        photo_optimization(self.image1)
        photo_optimization(self.image2)
        photo_optimization(self.image3)
        photo_optimization(self.image4)
        super(Products, self).save(*args, **kwargs)



    def jdate(self):
        return django_jalali(self.date)



    def percentage(self):
        if self.discounted_price !=0:
            number3 = self.discounted_price / self.price
            number3 = number3 * 100
            number4 = 100 - number3

            return f'{round(number4)}%'
        else:
            return 0

    def seller_info(self):
        seller = Sellers.objects.filter(id=self.seller.id).first()
        business_name = seller.business_name
        business_description = seller.business_description
        return [business_name,business_description]


    def __str__(self):
        return f'{self.title}'
    


class ProductsComments(models.Model):
    user = models.ForeignKey(Userperson,null=False, blank=False,on_delete=models.CASCADE,verbose_name='User')
    product = models.ForeignKey(Products,null=False, blank=False, on_delete=models.CASCADE,verbose_name='Prodcut Id')
    comment = models.TextField(null=False, blank=False,verbose_name='Comment')
    status = models.BooleanField(default=False, verbose_name='Status')
    date = models.DateTimeField(auto_now_add=True, blank=True, null=True, verbose_name='Date')

    def jdate(self):
        return django_jalali(self.date)


    def __str__(self):
        return f'{self.user}'

class ProductsTrackingCode(models.Model):
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



    
class ProductsScores(models.Model):
    product = models.ForeignKey(Products, on_delete=models.CASCADE, verbose_name='Prodcut ID', related_name='product')
    total_score = models.IntegerField(blank=False,verbose_name='"Total Score')

    def __str__(self):
        return f'{self.total_score}'


class ProductsSlides(models.Model):
    image = models.ImageField(upload_to='ProductsSlides',verbose_name='Image')
    url = models.URLField(verbose_name='Url')

    def save(self, *args, **kwargs):
        super(ProductsSlides, self).save(*args, **kwargs)
        if self.image:
            photo_optimization(self.image)
            super(ProductsSlides, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.url}"