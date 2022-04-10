from .serializers import SocialNetworksSerializers
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import SocialNetworks


@api_view(["GET"])
def social_networks(request):
    socialnetworks = SocialNetworks.objects.first()
    data = SocialNetworksSerializers(socialnetworks).data
    return Response(data)