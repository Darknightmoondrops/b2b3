from django.shortcuts import get_object_or_404, redirect, render
from .models import Products, ProductsComments
from extensions.products import specialProducts
from django.core.paginator import Paginator
from Sellers.models import Sellers 

"""
Views :

    product_list() # View all products per page
    product_detail() # View details of every product
    add_product() # product is added by seller
    remove_product() # prodcut is removed by seller
    
"""



def products_list_page(request):
    products = Products.objects.all()
    paginator = Paginator(products,1)
    page_number = request.GET.get('page')
    pages = paginator.get_page(page_number)
    special_products = Products.objects.filter(id__in=specialProducts())

    context = {
        'pages': pages,
        'special_products': special_products,
    }
    return render(request, 'Products/products_list_page/products_list_page.html', context)



def product_detail_page(request, slug):
    product = Products.objects.filter(slug=slug).first()
    # product = get_object_or_404(Products, title = title)
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



def add_product_page(request):
    if request.method == "POST":
        pass
    else:
        pass
    


def remove_product_page(request):
    pass