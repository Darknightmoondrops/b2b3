from .models import ServiceCategories,Services
from django.contrib import admin

@admin.register(ServiceCategories)
class ServiceCategoriesAdmin(admin.ModelAdmin):
    list_display = ['name','status']
    search_fields = ['name']
    
@admin.register(Services)
class ServicesAdmin(admin.ModelAdmin):
    list_display = ['service_user','date']
    search_fields = ['service_user']
    

