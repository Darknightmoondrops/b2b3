from django.urls import path
from . import views

app_name = 'Products'

urlpatterns =[
       path('', views.products_list_page, name = 'product_list_page'),
       path('detail/<slug:slug>/', views.product_detail_page, name = 'product_detail_page'), 
       path('add/', views.add_product_page, name = 'add_product_page'), 
       path('بنی/', views.remove_product_page, name='remove_product_page'),
]

