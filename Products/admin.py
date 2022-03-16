from django.contrib import admin
from .models import *


@admin.register(ProductsComments)
class ProductsCommentsAdmin(admin.ModelAdmin):
    list_display = ['user','status']

@admin.register(ProductMainCategories)
class ProductMainCategoriesAdmin(admin.ModelAdmin):
    list_display = ['name','status']


@admin.register(ProductSubCategories_1)
class ProductSubCategories_1Admin(admin.ModelAdmin):
    list_display = ['name','status']

@admin.register(ProductSubCategories_2)
class ProductSubCategories_2Admin(admin.ModelAdmin):
    list_display = ['name','status']


@admin.register(ProductsColor)
class ProductsColorAdmin(admin.ModelAdmin):
    list_display = ['name','code']

@admin.register(ProductsSizes)
class ProductsSizesAdmin(admin.ModelAdmin):
    list_display = ['name']

@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    list_display = ['title','price','date','score', 'slug','inventory']
    prepopulated_fields = {'slug': ('title',)}\

@admin.register(ProductsPhotos)
class ProductsPhotosAdmin(admin.ModelAdmin):
    list_display = ['product','image']

@admin.register(ProductsTrackingCode)
class ProductsTrackingCodeAdmin(admin.ModelAdmin):
    list_dislplay = ['tracking_code', 'product', 'code_status','product_status']

@admin.register(ProductsScores)
class ScoresAdmin(admin.ModelAdmin):
    list_display = ['product', 'total_score']

@admin.register(ProductsSlides)
class ProductsSlidesAdmin(admin.ModelAdmin):
    list_display = ['url']

