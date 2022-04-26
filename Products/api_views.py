from rest_framework.permissions import IsAuthenticated,IsSeller
from rest_framework.authtoken.models import Token
from django.shortcuts import get_object_or_404
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


class products_similar(generics.ListAPIView):
    serializer_class = ProdcutsSerializers

    def get_queryset(self):
        id = self.request.query_params.get('id')
        product = Products.objects.filter(id=id).first()
        return Products.objects.filter(maincategories__id__in=[ mainC.id for mainC in product.maincategories.all()]).all().order_by('id')


class product_next(generics.ListAPIView):
    serializer_class = ProdcutsSerializers

    def get_queryset(self):
        id = int(self.request.query_params.get('id'))
        return [get_object_or_404(Products,id=id+1)]


class product_previous(generics.ListAPIView):
    serializer_class = ProdcutsSerializers

    def get_queryset(self):
        id = int(self.request.query_params.get('id'))
        return [get_object_or_404(Products,id=id-1)]



class products_search(generics.ListAPIView):
    serializer_class = ProdcutsSerializers

    def get_queryset(self):
        q = self.request.query_params.get('q')
        return Products.objects.filter(title__icontains=q).all().order_by('id')


class products_sliders(generics.ListAPIView):
    queryset = ProductsSliders.objects.all().order_by('id')
    serializer_class = ProductsSlidersSerializers


class product_score(generics.CreateAPIView):
    serializer_class = ProductsScoresSerializers
    permission_classes = [IsAuthenticated]

    def post(self,request):
        data = ProductsScoresSerializers(data=request.data)
        if data.is_valid():
            if data.validated_data['score'] <=5 and  not(data.validated_data['score'] < 1) :
                user_token = str(request.headers['Authorization']).split('Token')[1].strip()
                token_info = Token.objects.filter(key=user_token).first()
                ProductsScores_check = ProductsScores.objects.filter(user_id=token_info.user.id,product_id=data.validated_data['product'].id).first()
                if ProductsScores_check is None:
                    ProductsScores(user_id=token_info.user.id, product_id=data.validated_data['product'].id,score=data.validated_data['score']).save()
                    return Response({'message': 'امتیاز ثبت شد'})
                else:
                    return Response({"message": "کاربر قبلا برای این محصول امتیاز ثبت کرده است"})
            else:
                return Response({'message': 'حداکثر امتیاز 5 است'})
        else:
            return Response(data.errors)


class products_filter(generics.ListAPIView):
    serializer_class = ProdcutsSerializers


    def get_queryset(self):
        price1 = self.request.query_params.get('price1')
        price2 = self.request.query_params.get('price2')
        categories = self.request.query_params.get('categories')
        colors = self.request.query_params.get('colors')
        sller_type = self.request.query_params.get('sller_type')
        return Products.objects.filter(Q(maincategories__name=categories) | Q(colors__products=colors) | Q(price=price1) | Q(price=price2) | Q(discounted_price=price1) | Q(discounted_price=price2) | Q(seller__business_categories=sller_type)).distinct().order_by('id')





class products_comments_list(generics.ListAPIView):
    serializer_class = ProductsCommentsSerializers

    def get_queryset(self):
        product_id = self.request.query_params.get('id')
        return ProductsComments.objects.filter(product_id=product_id).all()


class products_comments_add(generics.CreateAPIView):
    queryset = ProductsComments
    serializer_class = ProductsCommentsSerializers
    permission_classes = [IsAuthenticated]

    def post(self,request):
        data = ProductsCommentsSerializers(data=request.data)
        if data.is_valid():
            user_token = str(request.headers['Authorization']).split('Token')[1].strip()
            token_info = Token.objects.filter(key=user_token).first()
            productComments_check = ProductsComments.objects.filter(user_id=token_info.user.id,product_id=data.validated_data['product'].id,status=False).first()
            if productComments_check is None:
                ProductsComments(user_id=token_info.user.id, product_id=data.validated_data['product'].id,comment=data.validated_data['comment'], status=False).save()
                return Response({'message': 'دیدگاه ثبت شد'})
            else:
                return Response({"message": "کاربر قبلا برای این محصول دیدگاه ثبت کرده است"})
        else:
            return Response(data.errors)


class products_discounts(generics.ListAPIView):
    serializer_class = ProdcutsSerializers

    def get_queryset(self):

        return Products.objects.filter(id__in=latest_discounts_products()).order_by('id')



class products_offers(generics.ListAPIView):
    serializer_class = Products

    def get_queryset(self):
        return Products.objects.filter(id__in=specialProducts()).order_by('id')


class products_mostexpensive(generics.ListAPIView):
    serializer_class = ProdcutsSerializers

    def get_queryset(self):
        return Products.objects.filter(id__in=most_expensive_prodcuts()).order_by('id')



class products_cheapest(generics.ListAPIView):
    serializer_class = ProdcutsSerializers

    def get_queryset(self):
        return Products.objects.filter(id__in=cheapest_products()).order_by('id')



class products_bestselling(generics.ListAPIView):
    serializer_class = ProdcutsSerializers

    def get_queryset(self):
        return Products.objects.filter(id__in=BestSelling_products()).order_by('id')




class products_newest(generics.ListAPIView):

    serializer_class = ProdcutsSerializers

    def get_queryset(self):
        return Products.objects.order_by('-id').all()




class product_add(generics.CreateAPIView):
    serializer_class = ProdcutsSerializers
    permission_classes = [IsSeller]

    def post(self, request):

        data = ProdcutsSerializers(data=request.data)
        if data.is_valid():
            data.save()
            return Response({'message': 'محصول اضافه شد'})

        return Response(data.errors,status=status.HTTP_400_BAD_REQUEST)

