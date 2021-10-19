from import_export import resources
from .models import *


class WorkOrderResource(resources.ModelResource):
    class Meta:
        model = WorkOrder
        skip_unchanged = True
        report_skipped = False
        import_id_fields = ['number', 'title', 'content', 'type', 'status', 'is_show', 'is_return']
