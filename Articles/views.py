from .models import Articles,ArticlesHits,ArticlesLikes,ArticlesComments
from django.shortcuts import get_object_or_404,render,redirect
from extensions.articles import topArticles,visitor_ip_address
from CustomizedUserModel.models import Userperson
from django.core.paginator import Paginator
from SiteSettings.models import SiteSettings
from django.db.models import Q

"""

Views :

    articles_page() # View all articles And pagination
    article_page() # View an article
    
"""



def articles_list_page(request):
    site_settings = SiteSettings.objects.last()
    title = site_settings.site_name + " - " + "مقالات"


    context = {
        'title': title,
    }
    return render(request,'Articles/articles_list_page/articles_list_page.html',context)




def article_detail_page(request,id,slug):
    article = get_object_or_404(Articles,pk=id,slug=slug)
    visitor_ip_address(request,article.id)
    article_hits = ArticlesHits.objects.filter(article_id=article.id).count()
    site_settings = SiteSettings.objects.last()
    title = site_settings.site_name + " - " + f"{article.title}"
    like_count = ArticlesLikes.objects.filter(article_id=article.id).count()
    comment_count = ArticlesComments.objects.filter(article_id=article.id,status=True).count()
    comments = ArticlesComments.objects.filter(article_id=article.id,status=True).all()

    context = {
        'title': title,
        'article': article,
        'comments': comments,
        'article_hits': article_hits,
        'like_count': like_count,
        'comment_count': comment_count,
    }
    return render(request,'Articles/article_detail_page/article_detail_page.html',context)


def search_articles_page(request):
    try:
        search = request.GET['q']
    except:
        return redirect('Articles:articles_list_page')

    articles = Articles.objects.filter(Q(title=search) | Q(labels__name__icontains=search) | Q(description=search) | Q(short_description=search)).order_by('id').all()
    paginator = Paginator(articles, 12)
    page_number = request.GET.get('page')
    pages = paginator.get_page(page_number)
    latest_articles = Articles.objects.all().order_by('-id')[:5]
    top_articles = Articles.objects.filter(id__in=topArticles())


    context = {
        'latest_articles': latest_articles,
        'top_articles': top_articles,
        'pages': pages,
    }
    return render(request,'Articles/search_articles_page/search_articles_page.html',context)



