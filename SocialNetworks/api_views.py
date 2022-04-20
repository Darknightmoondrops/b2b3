from .serializers import SocialNetworksSerializers
from rest_framework import generics
from .models import SocialNetworks




class social_networks(generics.ListAPIView):
    serializer_class = SocialNetworksSerializers

    def get_queryset(self):
        return SocialNetworks.objects.first()