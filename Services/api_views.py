from rest_framework.decorators import api_view,permission_classes
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Q
from .serializers import *
from .models import *

@api_view(['GET'])
def services_list(request):
    paginator = PageNumberPagination()
    paginator.page_size = 12
    services = Services.objects.all().order_by('id')
    result_page = paginator.paginate_queryset(services, request)
    data = ServicesSerizalizers(result_page,many=True).data
    return paginator.get_paginated_response(data)


@api_view(['GET'])
def search_services(request):
    try:
        q = request.GET['q']
        services = Services.objects.filter(Q(title__icontains=q)).all().order_by('id')
        paginator = PageNumberPagination()
        paginator.page_size = 12
        result_page = paginator.paginate_queryset(services, request)
        data = ServicesSerizalizers(result_page, many=True).data
        return paginator.get_paginated_response(data)
    except:
        return Response({'message': 'error'},status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def services_filter(request):
    try:
        hour = request.GET['hour']
        gender = request.GET['gender']
        TypeOfCleaningSpace = request.GET['TypeOfCleaningSpace']
        company = request.GET['company']
        services = Services.objects.filter(type_of_cleaning_space__name=TypeOfCleaningSpace,service_user__gender=gender,company__icontains=company,service_reservation__hour__iexact=hour,service_reservation__status=False).all().order_by('id')
        paginator = PageNumberPagination()
        paginator.page_size = 12
        result_page = paginator.paginate_queryset(services, request)
        data = ServicesSerizalizers(result_page, many=True).data
        return paginator.get_paginated_response(data)
    except:
        return Response({'message': 'error'},status=status.HTTP_400_BAD_REQUEST)
