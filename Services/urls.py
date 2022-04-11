from django.urls import path
from . import views

app_name = 'Services'

urlpatterns = [
    path('services-list/',views.services_list_page,name='services_list_page'),
    path('detail/<int:id>/',views.service_detail_page,name='service_detail_page'),
]