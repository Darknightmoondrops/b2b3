from django.shortcuts import get_object_or_404, render
from .models import Products, ProductsComments
from django.core.paginator import Paginator

"""
Views :

    product_list() # View all products per page
    product_detail() # View details of every product
    
"""

def products_list_page(request):
    products = Products.objects.all()
    paginator = Paginator(products, 9)
    page_number = request.GET.get('page')
    pages = paginator.get_page(page_number)
    context = {
        'products' : products,
        'pages' : pages
        }
    return render(request, 'Products/products_list_page/products_list_page.html', context )


def product_detail_page(request, slug):
    product = get_object_or_404(Products, slug = slug)
    # comments = ProductsComments.objects.filter(product__in= product.id, status=True).all()
    try : 
        comments = ProductsComments.objects.get(product=product.title)
    except :
        comments = None 
    if request.method =='POST':
        new_comment = request.POST.get("new_comment")
        print(new_comment)
        if new_comment : 
          comments  =  ProductsComments.objects.create(comment=new_comment, status=False)
    context = {
        'product': product,
        'comments' : comments
    }
    return render(request, 'Products/product_detail_page/product_detail_page.html', context)