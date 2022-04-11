from django.urls import path
from . import views

app_name = 'UserPanel'

urlpatterns = [
    path('',views.userpanel_page,name='userpanel_page'),
    path('register/',views.userpanel_register_page,name='userpanel_register_page'),
    path('login/',views.userpanel_login_page,name='userpanel_login_page'),
    path('logout/',views.userpanel_logout_page,name='userpanel_logout_page'),
    path('code-authentication/<str:phone>/',views.code_authentication_page,name='code_authentication_page'),
]