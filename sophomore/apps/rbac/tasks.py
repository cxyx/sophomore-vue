from sophomore.celery import app
from celery import shared_task
import time


# 专属于myproject项目的任务
@app.task
def test():
    pass


@shared_task
def add():
    x, y = 1, 2
    with open('text.txt', mode='a', encoding="utf-8") as f:
        f.write(f'当前时间:{time.time()}')

        time.sleep(20)
    print(x)
    return x + y


@app.task(name='auto_aync_adpm')
def auto_aync_adpm():
    print('auto_aync_adpm')

    with open('text2.txt', mode='a', encoding="utf-8") as f:
        f.write(f'当前时间:{time.time()}')


@app.task(name='auto_aync_adpm1')
def auto_aync_adpm1():
    print('auto_aync_adpm1')

    with open('text2.txt', mode='a', encoding="utf-8") as f:
        f.write(f'当前时间:{time.time()}')


@app.task(name='auto_aync_adpm2')
def auto_aync_adpm2():
    with open('text2.txt', mode='a', encoding="utf-8") as f:
        f.write(f'当前时间:{time.time()}')
