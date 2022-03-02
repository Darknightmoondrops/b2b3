from django.contrib import admin
from .models import Articles

@admin.register(Articles)
class Articles(admin.ModelAdmin):
    list_display = ['writer','title','date']
