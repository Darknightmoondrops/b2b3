from django.urls import path
from . import api_views

app_name = 'ArticlesApi'

urlpatterns = [
    path('articles-list/',api_views.articles_list,name='articles_list'),
    path('search-articles/',api_views.search_articles,name='search_articles'),
    path('latest-articles/',api_views.latest_articles,name='latest_articles'),
    path('top-articles/',api_views.top_articles,name='top_articles'),
    path('add-articles-comment/',api_views.add_articles_comment,name='add_article_like'),
    path('add-article-like/',api_views.add_article_like,name='add_article_like'),
]