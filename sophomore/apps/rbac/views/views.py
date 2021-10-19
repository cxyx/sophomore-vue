from django.shortcuts import render
from django.http import HttpResponse
# from django.shortcuts import render, get_object_or_404, get_list_or_404  # todo:get_list_or_404
# from apps.personal.models import *
from apps.common.custom import get_object_or_404
# Create your views here.
# app/views1.py
from ..tasks import add
from ..serializers.menu_serializer import *
from ..serializers.organization_serializer import *
from ..serializers.permission_serializer import *
from ..serializers.role_serializer import *
from ..serializers.user_serializer import *
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.views import APIView
from rest_framework.response import Response

from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.permissions import IsAuthenticated
from ..models import *
from apps.common.custom import RbacPermission
from django.contrib.auth import get_user_model
from icecream import ic
from rest_framework.response import Response
from apps.common.loggers import l_logger
from rest_framework import viewsets
from rest_framework import generics
logger = l_logger(app_name="rbac")
test_logger = l_logger(app_name="rbac",module_name="test")
User = get_user_model()

def test_celery(request):
    for i in range(100):
        add.delay(3, 5)

    return HttpResponse("Celery works")


class MenuListView(ModelViewSet):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    filter_backends = (DjangoFilterBackend, OrderingFilter)
    filter_fields = ('name',)
    ordering_fields = ('id',)
    authentication_classes = (JSONWebTokenAuthentication,)
    permission_classes = (RbacPermission,)  # 是否有权限访问
    # filter_fields = ['']
    # search_fields = ['']
    # 部分网址用



class ProductViewSet(APIView):
    def get(self, request, format=None):

        return Response({
            'test':'ProductViewSet',
            'name':'ProductViewSet',
        })

class ImageViewSet(APIView):
    def get(self, request, format=None):

        return Response({
            'test':'ImageViewSet',
            'name':'ImageViewSet',
        })

from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import AllowAny
from ..serializers.jwt_serializers import MyTokenObtainPairSerializer

class MyObtainTokenPairView(TokenObtainPairView):
    permission_classes = (AllowAny,)
    serializer_class = MyTokenObtainPairSerializer


