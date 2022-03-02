from django.contrib import admin
from .models import SocialNetworks

@admin.register(SocialNetworks)
class SocialAdmin(admin.ModelAdmin):
    list_display = ('instagram','whatsapp','youtube','telegram','facebook' )

