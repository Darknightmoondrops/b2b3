from django.urls import path
from . import views
app_name = 'Articles'

urlpatterns = [
    path('',views.articles_list_page,name='articles_list_page'),
    path('<int:id>/',views.article_detail_page,name='article_detail_page'),
    path('add-article',views.add_article_page,name='add_article_page'),
]
