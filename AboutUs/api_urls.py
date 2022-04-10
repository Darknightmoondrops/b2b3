from django.urls import path
from . import api_views

app_name = 'ApiAboutUs'

urlpatterns = [
    path('',api_views.about_us,name='about_us'),
]