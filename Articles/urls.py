from django.urls import path
from . import views

app_name = 'Articles'

urlpatterns = [
    path('',views.articles_list_page,name='articles_list_page'),
    path('detail/<str:slug>/',views.article_detail_page,name='article_detail_page'),
    path('search/',views.search_articles_page,name='search_articles_page'),
    path('add-like/<int:id>/',views.add_article_like,name='add_article_like'),
]
