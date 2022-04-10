from django.urls import path
from  . import api_views

app_name = 'ApiSiteSettings'

urlpatterns = [
    path('',api_views.site_settings,name='site_settings'),
]