from rest_framework.decorators import api_view,permission_classes
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from extensions.products import *
from django.db.models import Q
from .serializers import *
from .models import *



@api_view(['GET'])
def products_list(request):
    paginator = PageNumberPagination()
    paginator.page_size = 12
    products = Products.objects.all().order_by('id')
    result_page = paginator.paginate_queryset(products, request)
    data = ProdcutsSerializers(result_page,many=True).data
    return paginator.get_paginated_response(data)


@api_view(['GET'])
def search_products(request):
    try:
        q = request.GET['q']
        articles = Products.objects.filter(Q(title__icontains=q)).all().order_by('id')
        paginator = PageNumberPagination()
        paginator.page_size = 12
        result_page = paginator.paginate_queryset(articles, request)
        data = ProdcutsSerializers(result_page, many=True).data
        return paginator.get_paginated_response(data)
    except:
        return Response({'message': 'error'},status=status.HTTP_400_BAD_REQUEST)\


@api_view(['GET'])
def products_filter(request):
    try:
        price = request.GET['price']
        categories = request.GET['categories']
        colors = request.GET['color']
        sller_type = request.GET['sller_type']
        articles = Products.objects.filter(Q(category__products=categories) | Q(colors__products=colors) | Q(price=price) | Q(seller__business_categories=sller_type)).all().order_by('id')
        paginator = PageNumberPagination()
        paginator.page_size = 12
        result_page = paginator.paginate_queryset(articles, request)
        data = ProdcutsSerializers(result_page, many=True).data
        return paginator.get_paginated_response(data)
    except:
        return Response({'message': 'error'},status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET'])
def products_comments_list(request):
    paginator = PageNumberPagination()
    paginator.page_size = 12
    products_comments = ProductsComments.objects.all()
    result_page = paginator.paginate_queryset(products_comments, request)
    data = ProductsCommentsSerializers(result_page,many=True).data
    return paginator.get_paginated_response(data)



@api_view(['POST'])
@permission_classes([IsAuthenticated])
def products_comments_add(request):
    try:
        data = ProductsCommentsSerializers(data=request.data)
        if data.is_valid():
            productComments_check = ProductsComments.objects.filter(user_id=data.validated_data['user'].id,product_id=data.validated_data['product'].id,status=False).first()
            if productComments_check is None:
                product = Products.objects.filter(id=data.validated_data['product'].id).first()
                ProductsComments(user_id=data.validated_data['user'].id, product_id=data.validated_data['product'].id,comment=data.validated_data['comment'], status=data.validated_data['status'],product_image=data.validated_data['product_image'], product_title=product.title,product_short_description=product.short_description).save()
                return Response({'message': 'Created successfully'})
            else:
                return Response({"message": "has been created"})
        else:
            return Response({"message": "Could not create, information is incorrect"})
    except:
        return Response({"message": "error"},status=status.HTTP_400_BAD_REQUEST)



@api_view(["GET"])
def products_discounts(request):
    LatestDiscountsProducts = Products.objects.filter(id__in=latest_discounts_products()).order_by('id')
    paginator = PageNumberPagination()
    paginator.page_size = 12
    result_page = paginator.paginate_queryset(LatestDiscountsProducts, request)
    data = ProdcutsSerializers(result_page,many=True).data
    return paginator.get_paginated_response(data)

@api_view(["GET"])
def products_offers(request):
    special_products = Products.objects.filter(id__in=specialProducts()).order_by('id')
    paginator = PageNumberPagination()
    paginator.page_size = 12
    result_page = paginator.paginate_queryset(special_products, request)
    data = ProductsCommentsSerializers(result_page,many=True).data
    return paginator.get_paginated_response(data)


@api_view(["GET"])
def products_mostexpensive(request):
    MostExpensiveProdcuts = Products.objects.filter(id__in=most_expensive_prodcuts()).order_by('id')
    paginator = PageNumberPagination()
    paginator.page_size = 12
    result_page = paginator.paginate_queryset(MostExpensiveProdcuts, request)
    data = ProductsCommentsSerializers(result_page,many=True).data
    return paginator.get_paginated_response(data)


@api_view(["GET"])
def products_cheapest(request):
    cheapestProducts = Products.objects.filter(id__in=cheapest_products()).order_by('id')
    paginator = PageNumberPagination()
    paginator.page_size = 12
    result_page = paginator.paginate_queryset(cheapestProducts, request)
    data = ProductsCommentsSerializers(result_page,many=True).data
    return paginator.get_paginated_response(data)



@api_view(["GET"])
def products_bestselling(request):
    best_selling_products = Products.objects.filter(id__in=BestSelling_products()).order_by('id')
    paginator = PageNumberPagination()
    paginator.page_size = 12
    result_page = paginator.paginate_queryset(best_selling_products, request)
    data = ProductsCommentsSerializers(result_page,many=True).data
    return paginator.get_paginated_response(data)



@api_view(["GET"])
def products_newest(request):
    products = Products.objects.order_by('-id').all()
    paginator = PageNumberPagination()
    paginator.page_size = 12
    result_page = paginator.paginate_queryset(products, request)
    data = ProductsCommentsSerializers(result_page,many=True).data
    return paginator.get_paginated_response(data)