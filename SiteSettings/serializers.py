from rest_framework import serializers
from .models import SiteSettings

class SiteSettingsSerializers(serializers.ModelSerializer):
    class Meta:
        model = SiteSettings
        fields = '__all__'
