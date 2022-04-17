from django.shortcuts import get_object_or_404,redirect, render
from SiteSettings.models import SiteSettings
from .models import *

"""
Views :

    product_list() # View all products per page
    product_detail() # View details of every product
    
"""



def products_list_page(request):
    site_settings = SiteSettings.objects.last()
    title = site_settings.site_name + " - " + "محصولات"

    context = {
        'title': title,
    }
    return render(request, 'Products/products_list_page/products_list_page.html', context)


def product_detail_page(request, id,slug):
    site_settings = SiteSettings.objects.last()
    product = get_object_or_404(Products,pk=id,slug=slug)
    title = site_settings.site_name + " - " + f"{product.title}"
    similar_products: Products = Products.objects.filter(category__in=[CategoryId for CategoryId in product.category.all()])
    next_product = Products.objects.filter(id=product.id+1).first()
    previous_product = Products.objects.filter(id=product.id-1).first()



    context = {
        'product': product,
        'title': title,
        'similar_products': similar_products,
        'next_product': next_product,
        'previous_product': previous_product,
    }



    return render(request, 'Products/product_detail_page/product_detail_page.html', context)



