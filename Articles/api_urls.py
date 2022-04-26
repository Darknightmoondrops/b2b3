from django.urls import path
from . import api_views

app_name = 'ArticlesApi'

urlpatterns = [
    path('articles-list/',api_views.articles_list.as_view(),name='articles_list'),
    path('articles-detail/',api_views.articles_detail.as_view(),name='articles_detail'),
    path('articles-search/',api_views.articles_search.as_view(),name='articles_search'),
    path('articles-latest/',api_views.articles_latest.as_view(),name='articles_latest'),
    path('articles-top/',api_views.articles_top.as_view(),name='articles_top'),
    path('articles-comment-add/',api_views.articles_comment_add.as_view(),name='articles_comment_add'),
    path('articles-comment-list/',api_views.articles_comment_list.as_view(),name='articles_comment_list'),
    path('articles-like-add/',api_views.articles_like_add.as_view(),name='articles_like_add'),
]
