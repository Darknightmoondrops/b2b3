from rest_framework.pagination import PageNumberPagination
from rest_framework import generics
from rest_framework import status
from django.db.models import Q
from .serializers import *
from .models import *


class services_list(generics.ListAPIView):
    serializer_class = ServicesSerizalizers
    pagination_class = PageNumberPagination

    def get_queryset(self):
        return Services.objects.all().order_by('id')



class search_services(generics.ListAPIView):
    serializer_class = ServicesSerizalizers
    pagination_class = PageNumberPagination

    def get_queryset(self):
        q = self.request.query_params.get('q')
        return Services.objects.filter(title__icontains=q).all().order_by('id')



class services_filter(generics.ListAPIView):
    serializer_class = ServicesSerizalizers
    pagination_class = PageNumberPagination

    def get_queryset(self):
        hour = self.request.query_params.get('hour')
        gender = self.request.query_params.get('gender')
        TypeOfCleaningSpace = self.request.query_params.get('TypeOfCleaningSpace')
        company = self.request.query_params.get('company')
        return Services.objects.filter(type_of_cleaning_space__name=TypeOfCleaningSpace,service_user__gender=gender,company__icontains=company,service_reservation__hour__iexact=hour,service_reservation__status=False).distinct().order_by('id')

