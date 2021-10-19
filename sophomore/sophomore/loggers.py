from loguru import logger
import time
import os

try:
    from django.contrib.auth import settings
    project_path = settings.BASE_DIR
except:
    print('\033[0;31;40m日志路径发生异常!\033[0m')
finally:
    project_path = '/Users/cx/workspace/sophomore'

def l_logger(app_name, module_name=''):
    # 如果是部分脱离整体 app 进行日志记录, 就加上一个参数, 不填都加到 app 整体日志下
    log_name = module_name if module_name else app_name
    log_path = f"{project_path}/apps/logs/{app_name}/{log_name}_log.log"

    logger.add(log_path,
               # format="{time:YYYY-MM-DD HH:mm:ss} | {message}",  # 日志记录格式
               # rotation="5 MB",   # 超过 5MB 生成新文件
               rotation="1 week",  # 每周生成新文件
               encoding="utf-8",  # 写入文件编码
               enqueue=True,  # 异步写入
               backtrace=True,  #
               diagnose=True,  # 显示堆栈报错信息
               retention="10 days"  # 保存时间
               )

    return logger

@logger.catch
def test_1():
    return 1/0

if __name__ == '__main__':
    logger = l_logger('personal')
    logger.info('test')
    logger.debug('test')
    logger.error('test')

    test_1()



