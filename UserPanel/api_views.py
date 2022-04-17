from rest_framework.decorators import api_view,permission_classes
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAdminUser
from CustomizedUserModel.models import Userperson
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Q
from .serializers import *
from .models import *


