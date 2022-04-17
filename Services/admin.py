from django.contrib import admin
from .models import *

@admin.register(ServicesTypeOfCleaningSpace)
class ServicesTypeOfCleaningSpaceAdmin(admin.ModelAdmin):
    list_display = ['name','status']
    search_fields = ['name']
    
@admin.register(Services)
class ServicesAdmin(admin.ModelAdmin):
    list_display = ['service_user','date']
    search_fields = ['service_user']


@admin.register(ServicesReservation)
class ServicesReservation(admin.ModelAdmin):
    list_display = ['service_user','hour']
    search_fields = ['service_user']


@admin.register(ServicesComments)
class ServicesCommentsAdmin(admin.ModelAdmin):
    list_display = ['user', 'date']
    search_fields = ['user','comment']