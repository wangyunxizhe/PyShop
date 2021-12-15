from celery.app import task
from celery_tasks.main import app
from utils.sendMessage import RongLianUtils

'''
celery生产者---任务
1，函数 celery_send_sms_code 必须让celery实例的task装饰器装饰
2，需要celery自动检测指定包的任务（这一步在celery_tasks/main.py里做了）
'''


@app.task
def celery_send_sms_code(sms_code, minute):
    # 使用容联云发送短信
    RongLianUtils().send_message(text=sms_code, minute=minute)
