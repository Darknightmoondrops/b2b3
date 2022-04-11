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

    def __str__(self):
        return f'{self.name}'


class ProductMainCategories(models.Model):
    name = models.CharField(max_length=999,verbose_name='Name')
    image = models.ImageField(upload_to='ProductMainCategoriesImage',blank=True,null=True,verbose_name='Image')
    status = models.BooleanField(default=False,verbose_name='Status')
    subCategories_1 = models.ManyToManyField(ProductSubCategories_1,blank=True,verbose_name='ProductSubCategories_1')
    
    def __str__(self):
        return f'{self.name}'
    



class ProductsColor(models.Model):
    name = models.CharField(max_length=150, blank=False)
    code = models.CharField(max_length=300)

    def __str__(self):
        return f'{self.name}'


class ProductsSizes(models.Model):
    name = models.CharField(max_length=150, blank=False)

    def __str__(self):
        return f'{self.name}'

# Products models
class Products(models.Model):
    title = models.CharField(max_length=999,blank=True,null=True,verbose_name='Title')
    slug = models.TextField(max_length=999)
    main_image = models.ImageField(upload_to='productsImage',blank=True,null=True,verbose_name='Image')
    image1 = models.ImageField(upload_to='productsImage',blank=True,null=True,verbose_name='Image1')
    image2 = models.ImageField(upload_to='productsImage',blank=True,null=True,verbose_name='Image2')
    image3 = models.ImageField(upload_to='productsImage',blank=True,null=True,verbose_name='Image3')
    image4 = models.ImageField(upload_to='productsImage',blank=True,null=True,verbose_name='Image4')
    image5 = models.ImageField(upload_to='productsImage',blank=True,null=True,verbose_name='Image5')
    description = models.TextField(verbose_name='Description')
    short_description = models.TextField(blank=True,null=True,verbose_name='Short Description')
    price = models.IntegerField(blank=True,null=True,verbose_name='Price')
    discounted_price = models.IntegerField(default=0,blank=True,null=True,verbose_name='Discounted Price')
    seller = models.ForeignKey(Sellers,on_delete=models.CASCADE,verbose_name='Seller')
    category = models.ManyToManyField(ProductMainCategories,blank=True,verbose_name='Category')
    colors = models.ManyToManyField(ProductsColor,blank=True,verbose_name='Colors')
    sizes = models.ManyToManyField(ProductsSizes,blank=True,verbose_name='Sizes')
    score = models.IntegerField(default=1,verbose_name='Score')
    date = models.DateTimeField(auto_now_add=True,blank=True,null=True,verbose_name='Date')
    inventory = models.IntegerField(default=0,blank=False,verbose_name='Inventory')

    def save(self, *args, **kwargs):
        super(Products, self).save(*args, **kwargs)
        if self.main_image:
            photo_optimization(self.main_image)
            super(Products, self).save(*args, **kwargs)
        if self.image1:
            photo_optimization(self.image1)
            super(Products, self).save(*args, **kwargs)

        if self.image2:
            photo_optimization(self.image2)
            super(Products, self).save(*args, **kwargs)

        if self.image3:
            photo_optimization(self.image3)
            super(Products, self).save(*args, **kwargs)

        if self.image4:
            photo_optimization(self.image4)
            super(Products, self).save(*args, **kwargs)

        if self.image5:
            photo_optimization(self.image5)
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

    def SubCategories_1(self):
        categories_id = [i.id for i in self.category.all()]
        product_mainCategories = ProductMainCategories.objects.filter(id__in=categories_id).first()
        categories = product_mainCategories.subCategories_1.all()
        return [category.name for category in categories]

    def __str__(self):
        return f'{self.title}'
    


class ProductsComments(models.Model):
    user = models.ForeignKey(Userperson,on_delete=models.CASCADE,verbose_name='User')
    status = models.BooleanField(default=False,verbose_name='Status')
    product_image = models.ImageField(upload_to='ProductsCommentsImage',blank=True,null=True,verbose_name='Image')
    product_title = models.TextField(blank=True,null=True,verbose_name='Title')
    product_short_description = models.TextField(blank=True,null=True,verbose_name='Short description')
    comment = models.TextField(verbose_name='Comment')
    product = models.ForeignKey(Products, on_delete=models.CASCADE, null=False, blank=False ,verbose_name='Prodcut Id')
    date = models.DateTimeField(auto_now_add=True, blank=True, null=True, verbose_name='Date')

    def save(self, *args, **kwargs):
        super(ProductsComments, self).save(*args, **kwargs)
        if self.product_image:
            photo_optimization(self.product_image)
            super(ProductsComments, self).save(*args, **kwargs)

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