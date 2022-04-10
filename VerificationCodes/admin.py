from django.contrib import admin
from .models import Codes

@admin.register(Codes)
class CodesAdmin(admin.ModelAdmin):
    list_filter = ['code']