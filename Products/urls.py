from django.urls import path
from . import views

app_name = 'Products'

urlpatterns =[
       path('', views.products_list_page,name='product_list_page'),
       path('detail/<str:slug>/', views.product_detail_page,name='product_detail_page'),
       path('search/', views.search_products_page,name='search_products_page'),
       path('order-by/', views.order_by_page,name='order_by_page'),
]

