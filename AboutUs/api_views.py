from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import AboutUsSerializers
from .models import AboutUs


@api_view(["GET"])
def about_us(request):
    aboutus = AboutUs.objects.first()
    data = AboutUsSerializers(aboutus).data
    return Response(data)