from rest_framework.decorators import api_view,permission_classes
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAdminUser
from CustomizedUserModel.models import Userperson
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Q
from .serializers import *
from .models import *




@api_view(['GET'])
@permission_classes([IsAdminUser])
def adminpanel_users(request):
    paginator = PageNumberPagination()
    paginator.page_size = 12
    users = Userperson.objects.filter(role='user').all().order_by('id')
    result_page = paginator.paginate_queryset(users, request)
    data = UsersSerializers(result_page,many=True).data
    return paginator.get_paginated_response(data)


@api_view(['GET'])
@permission_classes([IsAdminUser])
def adminpanel_admins(request):
    paginator = PageNumberPagination()
    paginator.page_size = 12
    admins = Userperson.objects.filter(role='admins').all().order_by('id')
    result_page = paginator.paginate_queryset(admins, request)
    data = UsersSerializers(result_page,many=True).data
    return paginator.get_paginated_response(data)

@api_view(['GET'])
@permission_classes([IsAdminUser])
def adminpanel_sellers(request):
    paginator = PageNumberPagination()
    paginator.page_size = 12
    seller = Userperson.objects.filter(role='seller').all().order_by('id')
    result_page = paginator.paginate_queryset(seller, request)
    data = UsersSerializers(result_page,many=True).data
    return paginator.get_paginated_response(data)



@api_view(['GET'])

def adminpanel_services(request):
    paginator = PageNumberPagination()
    paginator.page_size = 12
    services = Userperson.objects.filter(role='service').all().order_by('id')
    result_page = paginator.paginate_queryset(services, request)
    data = UsersSerializers(result_page,many=True).data
    return paginator.get_paginated_response(data)


@api_view(['POST'])
@permission_classes([IsAdminUser])
def adminpanel_add_user(request):
    data = UsersSerializers(data=request.data)
    if data.is_valid():
        if data.validated_data['role'] == 'admin':
            create_admin = Userperson.objects.create_superuser(fullname=data.validated_data['fullname'],phone=data.validated_data['phone'],role=data.validated_data['role'],gender=data.validated_data['gender'],image=data.validated_data['image'])
            create_admin.set_password(data.validated_data['password'])
            create_admin.save()
            return Response({'message': 'Admin was created'})
        else:
            create_user = Userperson.objects.create_user(fullname=data.validated_data['fullname'],phone=data.validated_data['phone'],role=data.validated_data['role'],gender=data.validated_data['gender'],image=data.validated_data['image'])
            create_user.set_password(data.validated_data['password'])
            create_user.is_staff = False
            create_user.save()
            return Response({'message': 'User created'})
    else:
        return Response(data.errors)


@api_view(['POST'])
@permission_classes([IsAdminUser])
def adminpanel_delete_user(request):
    try:
        user: Userperson = Userperson.objects.filter(id=request.POST['id']).first()
        user.delete()
        return Response({'message': 'User deleted'})
    except:
        return Response({'message': 'Error'})







