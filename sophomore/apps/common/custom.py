from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import BasePermission
from django.contrib.auth import get_user
from django.http import (
    Http404, HttpResponse, HttpResponsePermanentRedirect, HttpResponseRedirect,
)
from rest_framework.response import Response
from icecream import ic


class RbacPermission(BasePermission):

    def get_permission_from_role(self, request):
        return {}

    def has_permission(self, request, view):
        ic(request.user)
        request.user = get_user(request)
        ic(request.user)
        ic(request.user.is_authenticated)
        request_perms = self.get_permission_from_role(request)
        # if request_perms:

        return bool(request.user and request.user.is_authenticated)


def _get_queryset(klass):
    """
    Return a QuerySet or a Manager.
    Duck typing in action: any class with a `get()` method (for
    get_object_or_404) or a `filter()` method (for get_list_or_404) might do
    the job.
    """
    # If it is a model class or anything else with ._default_manager
    if hasattr(klass, '_default_manager'):
        return klass._default_manager.all()
    return klass


def get_object_or_404(klass, *args, **kwargs):
    # print('')
    # queryset = _get_queryset(klass)
    # if not hasattr(queryset, 'get'):
    #     klass__name = klass.__name__ if isinstance(klass, type) else klass.__class__.__name__
    #     raise ValueError(
    #         "First argument to get_object_or_404() must be a Model, Manager, "
    #         "or QuerySet, not '%s'." % klass__name
    #     )
    # try:
    #     return queryset.get(*args, **kwargs)
    # except queryset.model.DoesNotExist:
    #     print('执行了')
    #     # return Response({
    #     #     "出错了"
    #     # })

    return Response({
        'status':'tess'
    })

class BaseResponse(object):
    """
    初始化基本的返回数据信息
    """
    def __init__(self,status=True,data=None,error=None):
        self.status = status
        self.data = data
        self.error = error

    @property
    def get_data(self):
        return self.__dict__


if __name__ == '__main__':
    def get(self, request, version):
        ret = BaseResponse()  # 获取初始的数据信息
        try:
            # user_list = UserInfo.objects.all()
            # ser = IndexSerializer(user_list, many=True)
            ret.data = test.data
        except Exception as e:
            ret.status = False
            ret.error = '错误'
        return Response(ret.get_data)