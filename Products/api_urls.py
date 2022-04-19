from django.urls import path
from . import api_views

app_name = 'productApi'

urlpatterns = [
    path('products-list/',api_views.products_list.as_view(),name='products_list'),
    path('search-products/',api_views.search_products.as_view(),name='search_products'),
    path('products-filter/',api_views.products_filter.as_view(),name='products_filter'),
    path('products-comments-list/',api_views.products_comments_list.as_view(),name='products_comments_list'),
    path('products-comments-add/',api_views.products_comments_add.as_view(),name='products_comments_add'),
    path('products-discounts/',api_views.products_discounts.as_view(),name='products_discounts'),
    path('products-offers/',api_views.products_offers.as_view(),name='products_offers'),
    path('products-mostexpensive/',api_views.products_mostexpensive.as_view(),name='products_mostexpensive'),
    path('products-cheapest/',api_views.products_cheapest.as_view(),name='products_cheapest'),
    path('products-bestselling/',api_views.products_bestselling.as_view(),name='products_bestselling'),
    path('products-newest/',api_views.products_newest.as_view(),name='products_newest'),
    path('add-product/',api_views.add_product.as_view(),name='add_product'),
]