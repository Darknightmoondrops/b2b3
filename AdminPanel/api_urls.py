from django.urls import path
from . import api_views

app_name = 'ApiAdminPanel'

urlpatterns = [
    path('adminpanel-admins/', api_views.adminpanel_admins.as_view(), name='adminpanel_admins'),
    path('adminpanel-users/',api_views.adminpanel_users.as_view(),name='adminpanel_users'),
    path('adminpanel-sellers/',api_views.adminpanel_sellers.as_view(),name='adminpanel_sellers'),
    path('adminpanel-services/',api_views.adminpanel_services.as_view(),name='adminpanel_services'),
    path('adminpanel-add-user/',api_views.adminpanel_add_user.as_view(),name='adminpanel_add_user'),
    path('adminpanel-delete-user/',api_views.adminpanel_delete_user.as_view(),name='adminpanel_delete_user'),
]