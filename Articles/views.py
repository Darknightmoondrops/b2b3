from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator
from django.shortcuts import render
from .models import Articles


"""

Views :

    articles_page() # View all articles And pagination
    article_page() # View an article
    
"""



def articles_list_page(request):
    articles = Articles.objects.all()
    paginator = Paginator(articles, 12) 
    page_number = request.GET.get('page')
    pages = paginator.get_page(page_number)
    context = {
        'articles': articles,
        'pages': pages,
    }
    return render(request,'Articles/articles_list_page/articles_list_page.html',context)

def article_detail_page(request,id):
    article = get_object_or_404(Articles,id=id)
    context = {
        'article': article,
    }
    return render(request,'Articles/article_detail_page/article_detail_page.html',context)
