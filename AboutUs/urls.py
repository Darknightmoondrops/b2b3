from django.urls import path
from . import views

app_name = 'AboutUs'

urlpatterns = [
    path('about-us/',views.aboutus_page,name='aboutus_page'),
]
