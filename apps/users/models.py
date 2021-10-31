from django.db import models


# Create your models here.

# 1，自定义模型类：如有password这样的属性，密码需要自己加密，也需要自己实现登录时的密码验证
class User(models.Model):
    username = models.CharField(max_length=20, unique=True)
    password = models.CharField(max_length=20)
    mobile = models.CharField(max_length=11, unique=True)
