from django.urls import path
from . import views

app_name = 'Products'

urlpatterns =[
       path('', views.products_list_page, name = 'product_list_page'),
       path('<slug:slug>/', views.product_detail_page, name = 'product_detail_page')
]