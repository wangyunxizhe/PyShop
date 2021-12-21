from django.core.mail import send_mail

from celery_tasks.main import app


@app.task
def celery_send_email(subject, message, from_email, to_list, html_message):
    '''
    异步发送邮件
    '''
    # 调用django发送邮件模块的函数（相关配置在settings.py中）
    send_mail(subject=subject, message=message, from_email=from_email,
              recipient_list=to_list, html_message=html_message)
