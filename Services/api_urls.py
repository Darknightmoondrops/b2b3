from django.urls import path
from . import api_views

app_name = 'ApiServices'

urlpatterns = [
    path('services-list/', api_views.services_list, name='services_list'),
    path('search-services/', api_views.search_services, name='search_products'),
    path('services-filter/', api_views.services_filter, name='services_filter'),
    #path('services-comments-list/', api_views.services_comments_list, name='services_comments_list'),
    #path('services-comments-add/', api_views.services_comments_add, name='services_comments_add'),
]