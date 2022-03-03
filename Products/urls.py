from django.urls import path
from . import views

app_name = 'Products'

urlpatterns =[
       path('', views.products_list_page, name = 'product_list_page'),
       path('<slug:slug>/', views.product_detail_page, name = 'product_detail_page'), 
       path('add-product', views.add_product_page, name = 'add_product'), 
       path('remove', views.remove_product_page, name='remove_product'), 
       # path('invalid-user', views.invalid_user_page, name = 'invalid_user'),
       # path('not-Found', views.product_not_found_page, name = 'product_not_found'),
       # path('delete-successful', views.product_deleted_successfully_page, name = 'product_delete_successful'),
]