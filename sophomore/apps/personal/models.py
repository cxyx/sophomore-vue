from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()
# Create your models here.

'''
之前被限定住了

工单角色 : 用来为下拉筛选框提供可选择对象

工单权限 : 之前是当前处理人+工单状态 + 工单类型 = 工单权限
    设计思路两种 : 
        1. 设计工单权限表,根据工单状态+工单类型获取工单权限
        2. 直接在工单表中加字段
'''


class WorkOrder(models.Model):
    type_choices = (
        ('1', '环境申请'),
        ('2', '数据恢复'),
        ('3', '故障处理'),
        ('4', '服务请求'))

    status_choices = (
        ('1', '待提交'),
        ('2', '待审核'),
        ('3', '执行中'),
        ('4', '待脱敏'),
        ('5', '脱敏中'),
        ('6', '已脱敏'),
        ('7', '待确认'),
        ('8', '已关闭'))

    number = models.CharField(max_length=30, unique=True, verbose_name="工单号", help_text="工单号")
    title = models.CharField(max_length=30, unique=True, verbose_name="工单标题", help_text="工单标题")
    content = models.CharField(max_length=30, unique=True, verbose_name="工单内容", help_text="工单内容")
    # paso_name = models.ForeignKey(max_length=30, unique=True, verbose_name="工单内容",help_text="工单内容")
    type = models.CharField(max_length=30, choices=type_choices, default='0', verbose_name="工单类型", help_text="工单类型")
    status = models.CharField(max_length=30, choices=status_choices, default='0', verbose_name="工单状态", help_text="工单状态")
    is_show = models.BooleanField(blank=True, null=False, default=True, verbose_name='是否显示')
    is_return = models.BooleanField(blank=True, null=False, default=True, verbose_name='是否退回')
    add_time = models.DateTimeField(null=True, blank=True, verbose_name="创建时间")
    expect_time = models.DateTimeField(null=True, blank=True, verbose_name="期望时间")
    approve_time = models.DateTimeField(null=True, blank=True, verbose_name="审核时间")
    complete_time = models.DateTimeField(null=True, blank=True, verbose_name="完成时间")
    target_time = models.DateTimeField(null=True, blank=True, verbose_name="目标时间")
    # 上级
    up_todoer = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL,related_name='up_todoer',verbose_name='上级处理人')
    todoer = models.ForeignKey(User, null=True, on_delete=models.SET_NULL,related_name='todoer',verbose_name='当前处理人')
    proposer = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL,related_name='proposer',verbose_name='申请人')
    approver = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL,related_name='approver',verbose_name='初审人')
    final_approver = models.ForeignKey(User, blank=True, null=True,on_delete=models.SET_NULL,related_name='final_approver',verbose_name='终审人')

    class Meta:
        verbose_name = "工单信息"
        verbose_name_plural = verbose_name
        ordering = ['number']

    def __str__(self):
        return self.number

    @property
    def get_menus(self):
        def get_menu_config_dict():
            return {}

        todoer_roles = self.todoer.workorder_role.values_list()
        type = self.type
        status = self.status
        type = str(int(type) + 0.5) if "final_approve" in todoer_roles and 1 else type

        menu_list = get_menu_config_dict[type][status]

        return menu_list


class EnvCreateDetail(models.Model):
    project_number = models.CharField(max_length=30, null=True, blank=True, verbose_name="项目编号", help_text="项目编号")
    requirement_number = models.CharField(max_length=30, null=True, blank=True, verbose_name="需求编号",
                                          help_text="需求编号")
    file_content_resource = models.FileField(upload_to='file/%Y/%m/%d', null=True, blank=True, verbose_name="资源规划表",
                                             help_text="资源规划表")
    file_content_request = models.FileField(upload_to='file/%Y/%m/%d', null=True, blank=True, verbose_name="资源申请表",
                                            help_text="资源申请表")
    is_standard = models.BooleanField(null=True, blank=True, default=False, verbose_name="是否标准交付",
                                      help_text="是否标准交付")
    linkman = models.ForeignKey(User, related_name='link_man', null=True, blank=True, on_delete=models.SET_NULL,
                                verbose_name="接口人", help_text="接口人")

    class Meta:
        verbose_name = "环境新建详情"
        verbose_name_plural = verbose_name


class DbRecoveryOrder(models.Model):
    sensitive_choice = (
        ('1', '有敏感信息-脱敏'),
        ('2', '有敏感信息-不脱敏'),
        ('3', '无敏感信息')
    )

    redata_start_time = models.DateTimeField(null=True, blank=True, verbose_name="脱敏开始时间 1")
    safeman = models.ForeignKey(User, related_name='safeman', blank=True, null=True,
                                on_delete=models.SET_NULL, verbose_name='脱敏审核人', help_text="脱敏审核人")
    sensitive_type = models.CharField(max_length=10, choices=sensitive_choice, null=True, blank=True, default='3',
                                      verbose_name="敏感信息类型", help_text="敏感信息类型")
    oa_number = models.CharField(max_length=20, null=True, blank=True, verbose_name="OA编号", help_text="OA编号")
    data_extract_list = models.FileField(upload_to='file/%Y/%m/%d', null=True, blank=True, verbose_name="数据提取单",
                                         help_text="数据提取单")
    sensitive_info_form = models.FileField(upload_to='file/%Y/%m/%d', null=True, blank=True, verbose_name="敏感信息表",
                                           help_text="敏感信息表")
    oa_info_list = models.FileField(upload_to='file/%Y/%m/%d', null=True, blank=True, verbose_name="oa稿签表",
                                    help_text="oa稿签表")


class FaultResolveOrder(models.Model):
    priority_choices = (
        ('1', '普通'),
        ('2', '紧急'),
    )
    fault_choices = (
        ('1', 'HAC托管类'),
        ('2', '数据库类'),
        ('3', '操作系统类'),
        ('4', '其他类'),
    )

    hostenvs = models.CharField(max_length=500, null=True, blank=True, verbose_name="所有故障主机", help_text="所有故障主机")
    priority = models.CharField(max_length=10, choices=priority_choices, null=True, blank=True, verbose_name="紧急程度",
                                help_text="紧急程度")
    fault = models.CharField(max_length=10, choices=priority_choices, null=True, blank=True, verbose_name="故障类型",
                             help_text="故障类型")
    cause = models.TextField(max_length=50, null=True, blank=True, verbose_name="根本类型", help_text="根本类型")
    screenshot = models.FileField(upload_to='file/%Y/%m/%d', null=True, blank=True, verbose_name="故障截图",
                                  help_text="故障截图")

    class Meta:
        verbose_name = "故障解决详情"
        verbose_name_plural = verbose_name


class SubWorkOrder(models.Model):
    status_choices = (
        ('1', "新建待提交"),
        ('2', '处理中'),
        ('3', '已完成'),
        ('4', '已关闭')
    )

    number = models.CharField(max_length=30, unique=True, verbose_name="子工单号", help_text="子工单号")
    status = models.CharField(max_length=30, choices=status_choices, default='0', verbose_name="子工单状态",
                              help_text="子工单状态")
    work_order = models.ForeignKey(WorkOrder, on_delete=models.CASCADE, verbose_name='所属工单', help_text="所属工单")
    add_time = models.DateTimeField(null=True, blank=True, verbose_name="创建时间")
    complete_time = models.DateTimeField(null=True, blank=True, verbose_name="完成时间")
    content = models.TextField(null=True, blank=True, verbose_name="工单内容", help_text="工单内容")
    execution = models.TextField(null=True, blank=True, verbose_name="工单内容", help_text="完成情况")
    todoer = models.ForeignKey(User, related_name='todoer', blank=True, null=True, on_delete=models.SET_NULL,
                               verbose_name='处理人', help_text='处理人'),
    initiator = models.ForeignKey(User, related_name='initiator', blank=True, null=True, on_delete=models.SET_NULL,
                                  verbose_name='发起人', help_text='发起人')

    class Meta:
        verbose_name = "子工单信息"
        verbose_name_plural = verbose_name
        ordering = ['number']

    def __str__(self):
        return self.number

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.proposer = None


class WorkOrderDeliverRecord(models.Model):
    '''
    环境信息数据过大时,分批交付
    '''
    name = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL, verbose_name='交付人',
                             help_text="交付人")
    work_order = models.ForeignKey(WorkOrder, on_delete=models.CASCADE, verbose_name='所属工单', help_text="所属工单")
    # env_type = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL, verbose_name='交付人', help_text="交付人")
    add_time = models.DateTimeField(null=True, blank=True, verbose_name="创建时间")

    class Meta:
        verbose_name = "交付记录"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.work_order.number
