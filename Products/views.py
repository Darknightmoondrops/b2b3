from django.shortcuts import get_object_or_404, redirect, render
from .models import Products, ProductsComments, ProductCategories
from django.core.paginator import Paginator
from Sellers.models import Sellers 
from django.core.exceptions import PermissionDenied
from django.http import HttpResponse

"""
Views :

    product_list() # View all products per page
    product_detail() # View details of every product
    add_product() # product is added by seller
    remove_product() # prodcut is removed by seller
    
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
    seller_user = Sellers.objects.filter(business_status=True ,business_owner=request.user).first()
    if not seller_user:
        raise PermissionDenied('user is not seller')
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']  
        price = request.POST['price']  
        inventory = request.POST['inventory']
        category = ProductCategories.objects.get(name=request.POST['category'])
        seller = seller_user
        p_data = Products.objects.create(
                        title=title, 
                        description=description, 
                        price=price, 
                        inventory=inventory, 
                        seller = seller
                        )
        p_data.category.add(category)
        p_data.save()
    return render(request, 'Products/add_product_page/add_product_page.html')
    


def remove_product_page(request):
    seller_user = Sellers.objects.filter(business_owner=request.user,business_status=True).first()
    if not seller_user:
        raise PermissionDenied
    if request.method == 'POST':
        product = Products.objects.filter(title=request.POST['title']).first()
        if product: 
          product.delete()
          return HttpResponse('delet success')
        else : 
            return HttpResponse('not found')
    # else : 
    #     return redirect('not success template')
    return render(request, 'Products/remove_product_page/remove_product_page.html')


