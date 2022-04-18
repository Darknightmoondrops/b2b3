from rest_framework.decorators import api_view,permission_classes
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated,IsSeller
from rest_framework.authtoken.models import Token
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
        products = Products.objects.filter(Q(title__icontains=q)).all().order_by('id')
        paginator = PageNumberPagination()
        paginator.page_size = 12
        result_page = paginator.paginate_queryset(products, request)
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
    data = ProdcutsSerializers(result_page,many=True).data
    return paginator.get_paginated_response(data)


@api_view(["GET"])
def products_mostexpensive(request):
    MostExpensiveProdcuts = Products.objects.filter(id__in=most_expensive_prodcuts()).order_by('id')
    paginator = PageNumberPagination()
    paginator.page_size = 12
    result_page = paginator.paginate_queryset(MostExpensiveProdcuts, request)
    data = ProdcutsSerializers(result_page,many=True).data
    return paginator.get_paginated_response(data)


@api_view(["GET"])
def products_cheapest(request):
    cheapestProducts = Products.objects.filter(id__in=cheapest_products()).order_by('id')
    paginator = PageNumberPagination()
    paginator.page_size = 12
    result_page = paginator.paginate_queryset(cheapestProducts, request)
    data = ProdcutsSerializers(result_page,many=True).data
    return paginator.get_paginated_response(data)



@api_view(["GET"])
def products_bestselling(request):
    best_selling_products = Products.objects.filter(id__in=BestSelling_products()).order_by('id')
    paginator = PageNumberPagination()
    paginator.page_size = 12
    result_page = paginator.paginate_queryset(best_selling_products, request)
    data = ProdcutsSerializers(result_page,many=True).data
    return paginator.get_paginated_response(data)



@api_view(["GET"])
def products_newest(request):
    products = Products.objects.order_by('-id').all()
    paginator = PageNumberPagination()
    paginator.page_size = 12
    result_page = paginator.paginate_queryset(products, request)
    data = ProdcutsSerializers(result_page,many=True).data
    return paginator.get_paginated_response(data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def products_comments_add(request):
    data = ProductsCommentsSerializers(data=request.data)
    if data.is_valid():
        user_token = str(request.headers['Authorization']).split('Token')[1].strip()
        token_info = Token.objects.filter(key=user_token).first()
        productComments_check = ProductsComments.objects.filter(user_id=token_info.user.id,product_id=data.validated_data['product'].id,status=False).first()
        if productComments_check is None:
            ProductsComments(user_id=token_info.user.id, product_id=data.validated_data['product'].id,comment=data.validated_data['comment'], status=data.validated_data['status']).save()
            return Response({'message': 'Created successfully'})
        else:
            return Response({"message": "has been created"})
    else:
        return Response(data.errors)



@api_view(['POST'])
@permission_classes([IsSeller])
def add_product(request):
    print(request.data)
    data = ProdcutsSerializers(data=request.data)
    if data.is_valid():
        user_token = str(request.headers['Authorization']).split('Token')[1].strip()
        token_info = Token.objects.filter(key=user_token).first()
        seller = Sellers.objects.filter(business_owner_id=token_info.user.id).first()
        vl = data.validated_data
        # print(request.data)
        #
        # def validate(self, data):
        #     #print(data)
        #     try:
        #         d = data['sizes']
        #         print(d)
        #         return data
        #
        #     except:
        #         raise serializers.ValidationError({'sizes': ['این مقدار لازم است.']})

        # try:
        #     maincategories = str(request.POST['maincategories']).split(',')
        #     subCategories1 = str(request.POST['subCategories1']).split(',')
        #     subCategories2 = str(request.POST['subCategories2']).split(',')
        #     sizes = str(request.POST['sizes']).split(',')
        #     colors = str(request.POST['colors']).split(',')
        # except:
        #     return Response({'message': 'Required error not sent'},status=status.HTTP_400_BAD_REQUEST)

        product = Products.objects.create(seller_id=seller.id,title=vl['title'],slug=vl['slug'],main_image=vl['main_image'],image1=vl['image1'],image2=vl['image2'],image3=vl['image3'],image4=vl['image4'],description=vl['description'],short_description=vl['short_description'],price=vl['price'],discounted_price=vl['discounted_price'],inventory=vl['inventory'])

        # for maincategory in maincategories:
        #     product.maincategories.add(maincategory)
        #
        # for subcategory1 in subCategories1:
        #     product.subCategories1.add(subcategory1)
        #
        # for subcategory2 in subCategories2:
        #     product.subCategories2.add(subcategory2)
        #
        # for size in sizes:
        #     product.sizes.add(size)
        #
        # for color in colors:
        #     product.colors.add(color)

        product.save()

        return Response({'message': 'Product added'})
    else:
        return Response(data.errors)