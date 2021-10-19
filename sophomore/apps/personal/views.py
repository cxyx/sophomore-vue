from django.shortcuts import render, get_object_or_404, get_list_or_404  # todo:get_list_or_404
from django.contrib.auth import get_user_model
# Create your views here.
from rest_framework.views import APIView
from sophomore.loggers import l_logger
User = get_user_model()
from .menu_config import get_menu_list
from .models import *
from apscheduler.schedulers.background import BackgroundScheduler  # 使用它可以使你的定时任务在后台运行
from django_apscheduler.jobstores import DjangoJobStore, register_events, register_job
import time
from functools import wraps

logger = l_logger('personal')

'''
date：在您希望在某个特定时间仅运行一次作业时使用
interval：当您要以固定的时间间隔运行作业时使用
cron：以crontab的方式运行定时任务
minutes：设置以分钟为单位的定时器
seconds：设置以秒为单位的定时器
'''


try:
    scheduler = BackgroundScheduler()
    scheduler.add_jobstore(DjangoJobStore(), "default")

    @register_job(scheduler, "interval", seconds=5,replace_existing=True)
    def test_job():
        # 定时每5秒执行一次
        print(time.strftime('%Y-%m-%d %H:%M:%S'))

        with open('/Users/cx/workspace/sophomore/apps/personal/text.txt','a+') as f:
            f.write(f'当前时间{time.asctime()}\r\n')

    register_events(scheduler)
    # 启动定时器
    scheduler.start()
except Exception as e:
    print('定时任务异常：%s' % str(e))

