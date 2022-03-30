from django.urls import path
from . import views

app_name = 'Articles'

urlpatterns = [
    path('',views.articles_list_page,name='articles_list_page'),
    path('search/',views.search_articles_page,name='search_articles_page'),
    path('detail/<int:id>/<str:slug>/',views.article_detail_page,name='article_detail_page'),
]
