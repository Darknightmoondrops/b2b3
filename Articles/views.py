from asyncore import write
from audioop import error
from msilib.schema import Error
from multiprocessing import AuthenticationError
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator
from django.shortcuts import render
from .models import Articles
from CustomizedUserModel.models import Userperson
from django.core.exceptions import PermissionDenied


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

def add_article_page(request):
    user_object = Userperson.objects.filter(phone=request.user,is_superuser=True).first()

    if not user_object.is_superuser:
        raise PermissionDenied('user is not admin')

    if request.method == 'POST':
        title = request.POST['title']
        writer = user_object
        keywords = request.POST['keywords'] 
        description = request.POST['description']

        article = Articles.objects.create(
            title=title,
            writer=writer,
            keywords=keywords,
            description=description)
        article.save()
    return render(request,'Articles/add_article_page/add_article_page.html', )

