from django.shortcuts import get_object_or_404, redirect, render
from django.core.paginator import Paginator
from extensions.products import *
from django.db.models import Q
from .models import *

"""
Views :

    product_list() # View all products per page
    product_detail() # View details of every product
    
"""



def products_list_page(request):
    products = Products.objects.order_by('id').all()
    products_slides = ProductsSlides.objects.all()
    paginator = Paginator(products,1)
    page_number = request.GET.get('page')
    pages = paginator.get_page(page_number)
    special_products = Products.objects.filter(id__in=specialProducts())
    best_selling_products = Products.objects.filter(id__in=BestSelling_products())
    best_selling_categories = ProductMainCategories.objects.filter(id__in=BestSelling_categories())

    context = {
        'best_selling_categories': best_selling_categories,
        'best_selling_products': best_selling_products,
        'special_products': special_products,
        'products_slides': products_slides,
        'pages': pages,
        'count': products.count(),
    }
    return render(request, 'Products/products_list_page/products_list_page.html', context)





def search_products_page(request):
    try:
        search = request.GET['q']
    except:
        return redirect('Products:product_detail_page')
    products_slides = ProductsSlides.objects.all()
    products = Products.objects.filter(Q(title__icontains=search) | Q(description__icontains=search) | Q(category__name__icontains=search)).order_by('id').distinct()
    paginator = Paginator(products, 1)
    page_number = request.GET.get('page')
    pages = paginator.get_page(page_number)
    special_products = Products.objects.filter(id__in=specialProducts())
    best_selling_products = Products.objects.filter(id__in=BestSelling_products())
    best_selling_categories = ProductMainCategories.objects.filter(id__in=BestSelling_categories())


    context = {
        'best_selling_categories': best_selling_categories,
        'special_products': special_products,
        'best_selling_products': best_selling_products,
        'products_slides': products_slides,
        'pages': pages,
        'count': products.count(),
        'search': search,
        'order_by': 'جستجو',
    }
    return render(request,'Products/search_products_page/search_products_page.html',context)



# def order_by_page(request):
#     try:
#         orderBy = request.GET['q']
#     except:
#         return redirect('Products:product_list_page')
#
#     data = {
#         'newest': 'جدید ترین',
#         'bestselling': 'پرفروش ترین',
#         'cheapest': 'ارزان ترین',
#         'mostexpensive': 'گرانترین',
#         'offers': 'پیشنهادات',
#         'discounts': 'تخفیف ها',
#     }
#
#     special_products = Products.objects.filter(id__in=specialProducts()).order_by('id')
#     best_selling_products = Products.objects.filter(id__in=BestSelling_products()).order_by('id')
#     best_selling_categories = ProductMainCategories.objects.filter(id__in=BestSelling_categories()).order_by('id')
#
#     context = {
#         'best_selling_categories': best_selling_categories,
#         'special_products': special_products,
#         'best_selling_products': best_selling_products,
#         'pages': None,
#         'count': None,
#         'order_by': data.get(orderBy),
#         'search': orderBy,
#     }
#
#     if orderBy == 'newest':
#         products = Products.objects.order_by('-id').all()
#         paginator = Paginator(products, 12)
#         page_number = request.GET.get('page')
#         pages = paginator.get_page(page_number)
#         context['pages'] = pages
#         context['count'] = products.count()
#
#         return render(request, 'Products/search_products_page/search_products_page.html', context)
#
#     elif orderBy == 'bestselling':
#         paginator = Paginator(best_selling_products, 12)
#         page_number = request.GET.get('page')
#         pages = paginator.get_page(page_number)
#         context['pages'] = pages
#         context['count'] = best_selling_products.count()
#         return render(request, 'Products/search_products_page/search_products_page.html', context)
#
#     elif orderBy == 'cheapest':
#         cheapestProducts = Products.objects.filter(id__in=cheapest_products()).order_by('id')
#         paginator = Paginator(cheapestProducts, 12)
#         page_number = request.GET.get('page')
#         pages = paginator.get_page(page_number)
#         context['pages'] = pages
#         context['count'] = cheapestProducts.count()
#         return render(request, 'Products/search_products_page/search_products_page.html', context)
#
#     elif orderBy == 'mostexpensive':
#         MostExpensiveProdcuts = Products.objects.filter(id__in=most_expensive_prodcuts()).order_by('id')
#         paginator = Paginator(MostExpensiveProdcuts, 12)
#         page_number = request.GET.get('page')
#         pages = paginator.get_page(page_number)
#         context['pages'] = pages
#         context['count'] = MostExpensiveProdcuts.count()
#         return render(request, 'Products/search_products_page/search_products_page.html', context)
#
#     elif orderBy == 'offers':
#         paginator = Paginator(special_products, 12)
#         page_number = request.GET.get('page')
#         pages = paginator.get_page(page_number)
#         context['pages'] = pages
#         context['count'] = special_products.count()
#         return render(request, 'Products/search_products_page/search_products_page.html', context)
#
#     elif orderBy == 'discounts':
#         LatestDiscountsProducts = Products.objects.filter(id__in=latest_discounts_products()).order_by('id')
#         paginator = Paginator(LatestDiscountsProducts, 12)
#         page_number = request.GET.get('page')
#         pages = paginator.get_page(page_number)
#         context['pages'] = pages
#         context['count'] = LatestDiscountsProducts.count()
#         return render(request, 'Products/search_products_page/search_products_page.html', context)
#
#     else: return redirect('Products:product_list_page')
#



def product_detail_page(request, id,slug):
    product = get_object_or_404(Products,pk=id,slug=slug)
    products_photos = ProductsPhotos.objects.filter(product_id=product.id).all()
    similar_products: Products = Products.objects.filter(category__in=[CategoryId for CategoryId in product.category.all()])
    next_product = Products.objects.filter(id=product.id+1).first()
    previous_product = Products.objects.filter(id=product.id-1).first()



    context = {
        'product': product,
        'products_photos': products_photos,
        'similar_products': similar_products,
        'next_product': next_product,
        'previous_product': previous_product,
    }
    return render(request, 'Products/product_detail_page/product_detail_page.html', context)



