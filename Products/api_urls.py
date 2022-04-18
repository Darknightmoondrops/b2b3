from django.urls import path
from . import api_views

app_name = 'productApi'

urlpatterns = [
    path('products-list/',api_views.products_list,name='products_list'),
    path('search-products/',api_views.search_products,name='search_products'),
    path('products-filter/',api_views.products_filter,name='products_filter'),
    path('products-comments-list/',api_views.products_comments_list,name='products_comments_list'),
    path('products-comments-add/',api_views.products_comments_add,name='products_comments_add'),
    path('products-discounts/',api_views.products_discounts,name='products_discounts'),
    path('products-offers/',api_views.products_offers,name='products_offers'),
    path('products-mostexpensive/',api_views.products_mostexpensive,name='products_mostexpensive'),
    path('products-cheapest/',api_views.products_cheapest,name='products_cheapest'),
    path('products-bestselling/',api_views.products_bestselling,name='products_bestselling'),
    path('products-newest/',api_views.products_newest,name='products_newest'),
    path('add-product/',api_views.add_product,name='add_product'),
]