from django.apps import AppConfig


class RbacConfig(AppConfig):
    name = 'rbac'
    verbose_name = '权限管理系统'
    # def ready(self):
    #     from .signals import create_user
