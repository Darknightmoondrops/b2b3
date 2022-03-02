from django.contrib import admin
from .models import  SiteSettings

@admin.register(SiteSettings)
class SiteSettingAdmin(admin.ModelAdmin):
    list_display = ['site_name', 'contact_number', 'email']
    search_filter = ['site_name', 'contact_number']

