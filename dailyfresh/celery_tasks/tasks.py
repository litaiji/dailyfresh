from celery import Celery
from django.core.mail import send_mail
from dailyfresh import settings


import os
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "dailyfh.settings")
django.setup()


# 创建Celery实例
app = Celery('celery_tasks,tasks', broker='redis://182.92.87.221:6379/8')

# 定义任务函数
@app.task
def send_register_active_email(to_email, username, token):


    '''发送激活邮件'''
    # 组织邮件
    subject = '天天生鲜激活邮件'
    message = ''
    html_message = '<h1>尊敬的%s请点击该链接一激活您的账户</h1>http://182.92.87.221:8000/user/active/%s' % (username, token)
    from_email = settings.EMAIL_FROM
    recipient_list = [to_email]
    send_mail(subject=subject, message=message, from_email=from_email, recipient_list=recipient_list,
              html_message=html_message)
