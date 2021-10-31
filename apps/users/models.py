from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.

# 1，自定义模型类：如有password这样的属性，密码需要自己加密，也需要自己实现登录时的密码验证
# class User(models.Model):
#     username = models.CharField(max_length=20, unique=True)
#     password = models.CharField(max_length=20)
#     mobile = models.CharField(max_length=11, unique=True)

# 2，可以继承系统自带的User，因为系统已经实现了关于密码的加密和验证功能，在这个基础上再加入自己模型的属性
class User(AbstractUser):
    mobile = models.CharField(max_length=11, unique=True)

    # 设置表名的固定写法
    class Meta:
        db_table = 't_user_info'
        verbose_name = '用户管理'  # verbose_name属性为Django管理页面专用
        verbose_name_plural = verbose_name
