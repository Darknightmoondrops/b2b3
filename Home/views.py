from extensions.products import BestSelling_products,latest_discounts_products
from extensions.products import specialProducts
from django.shortcuts import render
from Articles.models import Articles
from Products.models import Products


def home_page(request):
    latest_articles = Articles.objects.all().order_by('-id')[:3]
    special_products = Products.objects.filter(id__in=specialProducts())
    best_selling_products = Products.objects.filter(id__in=BestSelling_products())
    LatestDiscountsProducts = Products.objects.filter(id__in=latest_discounts_products())




    context = {
        'latest_articles': latest_articles,
        'special_products': special_products,
        'best_selling_products': best_selling_products,
        'LatestDiscountsProducts': LatestDiscountsProducts,
    }
    return render(request,'Home/home_page/home_page.html',context)
