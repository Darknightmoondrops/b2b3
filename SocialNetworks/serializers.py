from rest_framework import serializers
from .models import SocialNetworks

class SocialNetworksSerializers(serializers.ModelSerializer):
    class Meta:
        model = SocialNetworks
        fields = ['instagram','whatsapp','youtube','telegram','facebook']