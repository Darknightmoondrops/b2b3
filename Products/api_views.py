from rest_framework.decorators import api_view,permission_classes
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .serializers import *
from .models import *


@api_view(['GET'])
def products_list(request):
    paginator = PageNumberPagination()
    paginator.page_size = 12
    products = Products.objects.all()
    result_page = paginator.paginate_queryset(products, request)
    data = ProdcutsSerializers(result_page,many=True).data
    return paginator.get_paginated_response(data)

@api_view(['GET'])
def products_comments_list(request):
    paginator = PageNumberPagination()
    paginator.page_size = 12
    products_comments = ProductsComments.objects.all()
    result_page = paginator.paginate_queryset(products_comments, request)
    data = ProductsCommentsSerializers(products_comments,many=True).data
    return paginator.get_paginated_response(data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def products_comments_add(request):
    data = ProductsCommentsSerializers(data=request.data)
    if data.is_valid():
        ProductsComments(user_id=data.validated_data['user'].id,product_id=data.validated_data['product'].id,comment=data.validated_data['comment'],status=data.validated_data['status']).save()
        return Response({'message': 'Created successfully'})
    else:
        return Response({"message": "Could not create, information is incorrect"})


