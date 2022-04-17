from django.urls import path
from . import api_views

app_name = 'ApiAdminPanel'

urlpatterns = [
    path('adminpanel-admins/', api_views.adminpanel_admins, name='adminpanel_admins'),
    path('adminpanel-users/',api_views.adminpanel_users,name='adminpanel_users'),
    path('adminpanel-sellers/',api_views.adminpanel_sellers,name='adminpanel_sellers'),
    path('adminpanel-services/',api_views.adminpanel_services,name='adminpanel_services'),
    path('adminpanel-add-user/',api_views.adminpanel_add_user,name='adminpanel_add_user'),
    path('adminpanel-delete-user/',api_views.adminpanel_delete_user,name='adminpanel_delete_user'),
]