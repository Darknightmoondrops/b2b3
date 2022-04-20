from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAdminUser
from CustomizedUserModel.models import Userperson
from rest_framework.response import Response
from rest_framework import generics
from rest_framework import status
from django.db.models import Q
from .serializers import *
from .models import *





class adminpanel_users(generics.ListAPIView):
    serializer_class = UsersSerializers
    pagination_class = PageNumberPagination
    permission_classes = [IsAdminUser]

    def get_queryset(self):
        return Userperson.objects.filter(role='user').all().order_by('id')



class adminpanel_admins(generics.ListAPIView):
    serializer_class = UsersSerializers
    pagination_class = PageNumberPagination
    permission_classes = [IsAdminUser]

    def get_queryset(self):
        return Userperson.objects.filter(role='admins').all().order_by('id')


class adminpanel_sellers(generics.ListAPIView):
    serializer_class = UsersSerializers
    pagination_class = PageNumberPagination
    permission_classes = [IsAdminUser]

    def get_queryset(self):
        return Userperson.objects.filter(role='seller').all().order_by('id')




class adminpanel_services(generics.ListAPIView):
    serializer_class = UsersSerializers
    pagination_class = PageNumberPagination
    permission_classes = [IsAdminUser]

    def get_queryset(self):
        return Userperson.objects.filter(role='service').all().order_by('id')





class adminpanel_add_user(generics.CreateAPIView):
    serializer_class = UsersSerializers
    pagination_class = PageNumberPagination
    permission_classes = [IsAdminUser]

    def post(self, request):
        data = UsersSerializers(data=request.data)
        if data.is_valid():
            if data.validated_data['role'] == 'admin':
                create_admin = Userperson.objects.create_superuser(fullname=data.validated_data['fullname'],phone=data.validated_data['phone'],role=data.validated_data['role'],gender=data.validated_data['gender'],image=data.validated_data['image'])
                create_admin.set_password(data.validated_data['password'])
                create_admin.is_staff = True
                create_admin.save()
                return Response({'message': 'Admin was created'})
            else:
                create_user = Userperson.objects.create_user(fullname=data.validated_data['fullname'],phone=data.validated_data['phone'],role=data.validated_data['role'],gender=data.validated_data['gender'],image=data.validated_data['image'])
                create_user.set_password(data.validated_data['password'])
                create_user.is_staff = True
                create_user.save()
                return Response({'message': 'User created'})
        else:
            return Response(data.errors)



class adminpanel_delete_user(generics.CreateAPIView):
    pagination_class = PageNumberPagination
    permission_classes = [IsAdminUser]

    def post(self, request):
        user_id = request.data.get('id')
        if user_id:
            user = Userperson.objects.filter(id=user_id).first()
            if user is not None:
                user.delete()
                return Response({'message': 'User deleted'})
            else:
                return Response({'message': 'کاربر وجود ندارد'})
        else:
            return Response({'id': 'این مقدار الزامی است'})








