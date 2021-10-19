import datetime
# 定时任务
import time


def confdict_handle():
    try:
        with open('./text.txt','w+',encoding='utf-8') as f:
            f.write(f'当前时间{time.asctime()}\r\n')

    except Exception as e:
        print('发生错误，错误信息为：', e)
