from rest_framework.permissions import IsAdminUser
from .serializers import SiteSettingsSerializers
from rest_framework import generics
from .models import SiteSettings



class site_settings(generics.ListAPIView):
    serializer_class = SiteSettingsSerializers
    permission_classes = [IsAdminUser]

    def get_queryset(self):
        return SiteSettings.objects.first()