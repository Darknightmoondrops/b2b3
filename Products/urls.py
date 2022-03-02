from django.urls import path
from . import views

app_name = 'Products'

urlpatterns =[
       path('', views.products_list_page, name = 'product_list_page'),
       path('<slug:slug>/', views.product_detail_page, name = 'product_detail_page'), 
       path('add', views.add_product, name = 'add_product'), 
       path('remove', views.remove_product, name='remove_product'), 
       path('invalid-user', views.invalid_user, name = 'invalid_user')
]