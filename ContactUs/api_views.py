from rest_framework.permissions import IsAdminUser
from .serializers import ContactUsSerizalizers
from rest_framework import generics
from .models import ContactUs




class contact_us(generics.ListAPIView):
    serializer_class = ContactUsSerizalizers
    permission_classes = [IsAdminUser]

    def get_queryset(self):
        return ContactUs.objects.all()