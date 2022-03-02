from django.contrib import admin
from .models import *


@admin.register(ProductsComments)
class ProductsCommentsAdmin(admin.ModelAdmin):
    list_display = ['user','status']

@admin.register(ProductCategories)
class ProductCategoriesAdmin(admin.ModelAdmin):
    list_display = ['name','status']


@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    list_display = ['title','price','date','score', 'slug','inventory']
    prepopulated_fields = {'slug': ('title',)}

@admin.register(TrackingCode)
class TrackingCodeAdmin(admin.ModelAdmin):
    list_dislplay = ['tracking_code', 'product', 'code_status','product_status']

@admin.register(Scores)
class ScoresAdmin(admin.ModelAdmin):
    list_display = ('product', 'total_score',)

