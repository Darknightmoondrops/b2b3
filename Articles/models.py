from CustomizedUserModel.models import Userperson
from extensions.DateJalali import django_jalali
from django.db import models


class ArticlesLabels(models.Model):
    name = models.CharField(max_length=999, verbose_name='Name')

    def __str__(self):
        return f'{self.name}'


class Articles(models.Model):
    title = models.CharField(max_length=999,verbose_name='Title')
    slug = models.TextField(blank=True,null=True,verbose_name='Slug')
    image = models.ImageField(upload_to='articlesImage',blank=True,null=True,verbose_name='Image')
    writer = models.ForeignKey(Userperson,on_delete=models.CASCADE,blank=True,null=True,verbose_name='Writer')
    date = models.DateField(auto_now_add=True,verbose_name='Date')
    keywords = models.TextField(verbose_name='Keywords')
    description = models.TextField(verbose_name='Description', default='a  description')
    short_description = models.TextField(blank=True,null=True,verbose_name='Short description', default='a short description')
    labels = models.ManyToManyField(ArticlesLabels,verbose_name='Labels')

    @property
    def writer_fullname(self):
        return self.writer.fullname

    @property
    def jdate(self):
        return django_jalali(self.date)
    
    def __str__(self):
        return f'{self.title}'





class ArticlesHits(models.Model):
    article = models.ForeignKey(Articles,on_delete=models.CASCADE,blank=True,null=True,verbose_name='Article')
    ip = models.CharField(max_length=30,verbose_name='IP')

    def __str__(self):
        return f'{self.ip}'

class ArticlesLikes(models.Model):
    like = models.ForeignKey(Userperson,on_delete=models.CASCADE,verbose_name='Like')
    article = models.ForeignKey(Articles,on_delete=models.CASCADE,blank=True,null=True,verbose_name='Article')

    def __str__(self):
        return f'{self.like}'


class ArticlesComments(models.Model):
    user = models.ForeignKey(Userperson,on_delete=models.CASCADE,verbose_name='User')
    article = models.ForeignKey(Articles, on_delete=models.CASCADE, blank=True, null=True, verbose_name='Article')
    first_name = models.CharField(max_length=999,blank=True,null=True,verbose_name='First Name')
    last_name = models.CharField(max_length=999,blank=True,null=True,verbose_name='last_name')
    comment = models.TextField(verbose_name='Comment')
    status = models.BooleanField(default=False,blank=True,null=True,verbose_name='Status')
    date = models.DateField(auto_now_add=True,blank=True,null=True, verbose_name='Date')

    def __str__(self):
        return f'{self.user}'


    def jdate(self):
        return django_jalali(self.date)