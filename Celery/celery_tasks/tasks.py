
from celery import Celery
from django.template import loader
from django.core.mail import send_mail
from dailyfresh import settings

import os
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "dailyfresh.settings")
django.setup()

from goods.models import GoodsType
from goods.models import IndexPromotionBanner
from goods.models import IndexTypeGoodsBanner
from goods.models import IndexGoodsBanner


# 创建Celery实例


app = Celery('celery_tasks.task', broker='redis://182.92.87.221:6379/8')
# app = Celery('celery_tasks,tasks', broker='redis://10.0.125.178:6379/8')
# app = Celery('celery_tasks,tasks', broker='redis://10.0.128.126:6379/8')


# 定义发送邮件异步任务函数
@app.task
def send_register_active_email(to_email, username, token):
    '''发送激活邮件'''
    # 组织邮件
    subject = '天天生鲜激活邮件'
    message = '111'
    html_message = '<h1>尊敬的%s请点击该链接一激活您的账户</h1>http://182.92.87.221:8000/user/active/%s' % (username, token)
    from_email = settings.EMAIL_FROM
    recipient_list = [to_email]
    send_mail(subject=subject, message=message, from_email=from_email, recipient_list=recipient_list,
              html_message=html_message)


# 定义生成静态页面异步任务函数
@app.task
def generate_static_index_html():
    '''
    产生首页静态页面
    :return:
    '''
    '''显示首页'''
    # 获取商品种类信息
    types = GoodsType.objects.all()

    # 获取首页轮播商品信息
    goods_banners = IndexGoodsBanner.objects.all().order_by('index')

    # 获取首页商品促销活动信息
    promotin_banners = IndexPromotionBanner.objects.all().order_by('index')

    # 获取首页分类商品展示信息
    for type in types:
        # 获取type种类首页分类商品的图片信息
        image_banners = IndexTypeGoodsBanner.objects.filter(type=type, display_type=1).order_by('index')

        # 获取type种类首页分类商品的文字信息
        title_banners = IndexTypeGoodsBanner.objects.filter(type=type, display_type=0).order_by('index')

        # 动态给type增加属性，分别保存首页分类商品的图片展示信息和文字展示信息
        type.image_banners = image_banners
        type.title_banners = title_banners

    # 组织上下文
    context = {
        'types': types,
        'goods_banners': goods_banners,
        'promotin_banners': promotin_banners,
    }

    # 使用模板
    # 1.加载模板文件,返回模板对象
    temp = loader.get_template('static_index.html')
    # context = RequestContext(request, context)
    # 2.模板渲染
    static_index_html = temp.render(context)
    # 生成首页对应的静态文件
    save_path = os.path.join(settings.BASE_DIR, 'static/index.html')
    with open(save_path, 'w') as fp:
        fp.write(static_index_html)
