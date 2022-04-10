from django.urls import path
from . import api_views


app_name = 'ApiContactUs'

urlpatterns = [
    path('',api_views.contact_us,name='contact_us'),
]