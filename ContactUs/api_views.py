from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAdminUser
from .serializers import ContactUsSerizalizers
from rest_framework.response import Response
from .models import ContactUs



@api_view(["GET"])
@permission_classes([IsAdminUser])
def contact_us(request):
    contactus = ContactUs.objects.all()
    data = ContactUsSerizalizers(contactus,many=True).data
    return Response(data)