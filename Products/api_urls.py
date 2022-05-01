from django.urls import path
from . import api_views

app_name = 'productsApi'

urlpatterns = [
    path('products-list/',api_views.products_list.as_view(),name='products_list'),
    path('products-detail/',api_views.products_detail.as_view(),name='products_detail'),
    path('products-similar/',api_views.products_similar.as_view(),name='products_similar'),
    path('products-next/',api_views.product_next.as_view(),name='product_next'),
    path('products-previous/',api_views.product_previous.as_view(),name='product_previous'),
    path('products-sliders/',api_views.products_sliders.as_view(),name='products_sliders'),
    path('products-search/',api_views.products_search.as_view(),name='products_search'),
    path('products-filter/',api_views.products_filter.as_view(),name='products_filter'),
    path('products-filter-category/',api_views.products_filter_category.as_view(),name='products_filter_category'),
    path('products-main-categories/',api_views.products_main_categories.as_view(),name='products_main_categories'),
    path('products-colors/',api_views.products_colors.as_view(),name='products_colors'),
    path('products-sellers-types/',api_views.products_sellers_typs.as_view(),name='products_sellers_typs'),
    path('products-comments-list/',api_views.products_comments_list.as_view(),name='products_comments_list'),
    path('products-discounts/',api_views.products_discounts.as_view(),name='products_discounts'),
    path('products-offers/',api_views.products_offers.as_view(),name='products_offers'),
    path('products-mostexpensive/',api_views.products_mostexpensive.as_view(),name='products_mostexpensive'),
    path('products-cheapest/',api_views.products_cheapest.as_view(),name='products_cheapest'),
    path('products-bestselling/',api_views.products_bestselling.as_view(),name='products_bestselling'),
    path('products-newest/',api_views.products_newest.as_view(),name='products_newest'),
    path('products-score-info/', api_views.products_score_info.as_view(),name='product_score_info'),
    path('products-add/',api_views.products_add.as_view(),name='product_add'),
    path('products-score-add/', api_views.products_score_add.as_view(),name='product_score_add'),
    path('products-comments-add/', api_views.products_comments_add.as_view(),name='products_comments_add'),
]