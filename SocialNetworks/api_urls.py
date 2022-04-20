from django.urls import path
from . import api_views

app_name = 'ApiSocialNetworks'

urlpatterns = [
    path('',api_views.social_networks.as_view(),name='social_networks'),
]