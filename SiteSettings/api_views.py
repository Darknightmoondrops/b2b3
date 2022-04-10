from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAdminUser
from .serializers import SiteSettingsSerializers
from rest_framework.response import Response
from .models import SiteSettings

@api_view(['GET'])
@permission_classes([IsAdminUser])
def site_settings(request):
    sitesettings = SiteSettings.objects.first()
    data = SiteSettingsSerializers(sitesettings).data
    return Response(data)