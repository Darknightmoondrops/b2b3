from django.urls import path
from . import api_views

app_name = 'productApi'

urlpatterns = [
    path('products-list/',api_views.products_list,name='products_list'),
    path('products-comments-list/',api_views.products_comments_list,name='products_comments_list'),
    path('products-comments-add/',api_views.products_comments_add,name='products_comments_add'),
]