import os
from celery import Celery
from celery.schedules import crontab, schedule
from django.utils import timezone
from django.conf import settings
# 设置环境变量
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sophomore.settings')

# 实例化
app = Celery('sophomore')

# namespace='CELERY'作用是允许你在Django配置文件中对Celery进行配置
# 但所有Celery配置项必须以CELERY开头，防止冲突
app.config_from_object('django.conf:settings', namespace='CELERY')

# 自动从Django的已注册app中发现任务
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
# 可单独创建
# app.autodiscover_tasks(['celery_email'], force=True)
# 时区
# app.conf.timezone = "Asia/Shanghai"
# 是否使用 UTC
# app.conf.enable_utc = False

# 解决时区问题,定时任务启动就循环输出
# app.now = timezone.now

# 下面的任务执行条件有一下几点
# 1. 启动 django
# 2. celery -A $project_name -B -l info
# app.conf.celery_import
app.conf.beat_schedule = {
    # 定时执行,15:36 执行
    'sync_admin_daily': {
        'task': 'auto_aync_adpm',
        'schedule': crontab(minute=36, hour=15)
    },
    'sync_admin_daily2': {
        'task': 'auto_aync_adpm1',
        'schedule': crontab(minute=1) , # run every 6 minute
        # 'schedule': crontab(minute=0, hour="12,14,15,16,17,18,20,22,0,2"), # -6 to get Dallas time
        # 'schedule':crontab(minute=0, hour=18, day_of_week="1,3,5"),# Monday,Wendesday,Friday at 8AM Dallas time
        # 'schedule': crontab(minute=0, hour=14),  # Monday,Wendesday,Friday at 8AM Dallas time
        # 'schedule': crontab(minute=0,),  # Monday,Wendesday,Friday at 8AM Dallas time

    },
    'sync_admin_daily3': {
        'task': 'auto_aync_adpm2',
        'schedule': crontab(minute='*/1') , # run every 6 minute]
    },
    'add_test': {
        'task': 'apps.rbac.tasks.add',
        'schedule': crontab(minute='1') , # run every 6 minute]

    },
}

# app.conf.broker_transport_options = {
#     "max_retries": 3,  # 最大开始时间
#     "interval_start": 0,
#     "interval_step": 0.2,
#     "interval_max": 0.5,
# }
# 一个测试任务
# @app.task(bind=True)
# def debug_task(self):
#     print(f'Request: {self.request!r}')
