from rest_framework.decorators import api_view,permission_classes
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated,IsSeller
from django.core.exceptions import ValidationError
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import generics
from rest_framework import status
from extensions.products import *
from django.db.models import Q
from .serializers import *
from .models import *


class products_list(generics.ListAPIView):
    queryset = Products.objects.all().order_by('id')
    serializer_class = ProdcutsSerializers
    pagination_class = PageNumberPagination





class search_products(generics.ListAPIView):
    serializer_class = ProdcutsSerializers
    pagination_class = PageNumberPagination

    def get_queryset(self):
        q = self.request.query_params.get('q')
        print(q)
        return Products.objects.filter(title__icontains=q).all().order_by('id')




class products_filter(generics.ListAPIView):
    serializer_class = ProdcutsSerializers
    pagination_class = PageNumberPagination


    def get_queryset(self):
        price1 = self.request.query_params.get('price1')
        price2 = self.request.query_params.get('price2')
        categories = self.request.query_params.get('categories')
        colors = self.request.query_params.get('colors')
        sller_type = self.request.query_params.get('sller_type')
        return Products.objects.filter(Q(maincategories__name=categories) | Q(colors__products=colors) | Q(price=price1) | Q(price=price2) | Q(discounted_price=price1) | Q(discounted_price=price2) | Q(seller__business_categories=sller_type)).distinct().order_by('id')





class products_comments_list(generics.ListAPIView):
    serializer_class = ProductsCommentsSerializers
    pagination_class = PageNumberPagination

    def get_queryset(self):
        product_id = self.request.query_params.get('id')
        return ProductsComments.objects.filter(product_id=product_id).all()


class products_comments_add(generics.CreateAPIView):
    queryset = ProductsComments
    serializer_class = ProductsCommentsSerializers
    pagination_class = PageNumberPagination
    permission_classes = [IsAuthenticated]

    def post(self,request):
        data = ProductsCommentsSerializers(data=request.data)
        if data.is_valid():
            user_token = str(request.headers['Authorization']).split('Token')[1].strip()
            token_info = Token.objects.filter(key=user_token).first()
            productComments_check = ProductsComments.objects.filter(user_id=token_info.user.id,product_id=data.validated_data['product'].id,status=False).first()
            if productComments_check is None:
                ProductsComments(user_id=token_info.user.id, product_id=data.validated_data['product'].id,comment=data.validated_data['comment'], status=False).save()
                return Response({'message': 'دیدگاه اضافه شد'})
            else:
                return Response({"message": "کاربر قبلا برای این محصول دیدگاه ثبت کرده است"})
        else:
            return Response(data.errors)


class products_discounts(generics.ListAPIView):
    serializer_class = Products
    pagination_class = PageNumberPagination

    def get_queryset(self):

        return Products.objects.filter(id__in=latest_discounts_products()).order_by('id')



class products_offers(generics.ListAPIView):
    serializer_class = Products
    pagination_class = PageNumberPagination

    def get_queryset(self):
        return Products.objects.filter(id__in=specialProducts()).order_by('id')


class products_mostexpensive(generics.ListAPIView):
    serializer_class = Products
    pagination_class = PageNumberPagination

    def get_queryset(self):
        return Products.objects.filter(id__in=most_expensive_prodcuts()).order_by('id')



class products_cheapest(generics.ListAPIView):
    serializer_class = Products
    pagination_class = PageNumberPagination

    def get_queryset(self):
        return Products.objects.filter(id__in=cheapest_products()).order_by('id')



class products_bestselling(generics.ListAPIView):
    serializer_class = Products
    pagination_class = PageNumberPagination

    def get_queryset(self):
        return Products.objects.filter(id__in=BestSelling_products()).order_by('id')




class products_newest(generics.ListAPIView):

    serializer_class = Products
    pagination_class = PageNumberPagination

    def get_queryset(self):
        return Products.objects.order_by('-id').all()




class add_product(generics.CreateAPIView):
    serializer_class = ProdcutsSerializers
    permission_classes = [IsSeller]

    def post(self, request):

        data = ProdcutsSerializers(data=request.data)
        if data.is_valid():
            data.save()
            return Response({'message': 'محصول اضافه شد'})

        return Response(data.errors,status=status.HTTP_400_BAD_REQUEST)

