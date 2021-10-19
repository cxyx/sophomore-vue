from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .resource import *
from django.http import JsonResponse

admin.site.site_header = 'sophomore管理后台'  # 设置header
admin.site.site_title = 'sophomore管理后台'  # 设置title
admin.site.index_title = 'sophomore管理后台'

# Register your models here.
# admin.site.register(models.UserProfile)
# admin.site.register(models.Permission)
# admin.site.register(models.Organization)
# admin.site.register(models.Role)
# admin.site.register(models.Menu)
from simpleui.admin import AjaxAdmin


@admin.register(WorkOrder)
class WorkOrderAdmin(ImportExportModelAdmin,AjaxAdmin):
    resource_class = WorkOrderResource
    list_display = ['number', 'title', 'content', 'type', 'status']
    search_fields = ['number', 'title', 'content', 'type', 'status']
    list_filter = ['number']
    list_per_page = 100

    actions = ['make_copy', 'custom_button']

    def custom_button(self, request, queryset):
        pass

    # 显示的文本，与django admin一致
    custom_button.short_description = '测试按钮'
    # icon，参考element-ui icon与https://fontawesome.com
    custom_button.icon = 'fas fa-audio-description'

    # 指定element-ui的按钮类型，参考https://element.eleme.cn/#/zh-CN/component/button
    custom_button.type = 'danger'

    # 给按钮追加自定义的颜色
    custom_button.style = 'color:black;'

    def make_copy(self, request, queryset):
        pass

    make_copy.short_description = '复制员工'

