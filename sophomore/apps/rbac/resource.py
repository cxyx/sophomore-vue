from import_export import resources
from .models import *


class MenuResource(resources.ModelResource):
    class Meta:
        model = Menu
        skip_unchanged = True
        report_skipped = False
        import_id_fields = ['name', 'icon', 'path', 'is_frame', 'is_show', 'sort', 'component', 'pid']


class PermissionResource(resources.ModelResource):
    class Meta:
        model = Permission
        skip_unchanged = True
        report_skipped = False
        import_id_fields = ['name', 'method', 'pid']


class RoleResource(resources.ModelResource):
    class Meta:
        model = Role
        skip_unchanged = True
        report_skipped = False
        import_id_fields = ['name', 'permissions', 'menus', 'desc']


class OrganizationResource(resources.ModelResource):
    class Meta:
        model = Organization
        skip_unchanged = True
        report_skipped = False
        import_id_fields = ['name', 'type', 'pid']


class UserProfileResource(resources.ModelResource):
    class Meta:
        model = UserProfile
        skip_unchanged = True
        report_skipped = False
        import_id_fields = ['name', 'mobile', 'email', 'image', 'department', 'position', 'superior', 'roles']


class WorkorderRoleResource(resources.ModelResource):
    class Meta:
        model = WorkorderRole
        skip_unchanged = True
        report_skipped = False
        import_id_fields = ['name', 'desc']
