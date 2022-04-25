from django.urls import path
from . import api_views

app_name = 'ArticlesApi'

urlpatterns = [
    path('articles-list/',api_views.articles_list.as_view(),name='articles_list'),
    path('article-detail/',api_views.article_detail.as_view(),name='article_detail'),
    path('search-articles/',api_views.search_articles.as_view(),name='search_articles'),
    path('latest-articles/',api_views.latest_articles.as_view(),name='latest_articles'),
    path('top-articles/',api_views.top_articles.as_view(),name='top_articles'),
    path('add-articles-comment/',api_views.add_articles_comment.as_view(),name='add_article_like'),
    path('add-article-like/',api_views.add_article_like.as_view(),name='add_article_like'),
]