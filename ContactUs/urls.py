from django.urls import path
from  . import views

app_name = 'ContactUs'

urlpatterns = [
    path('',views.contactus_page,name='contactus_page')
]
