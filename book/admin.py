from django.contrib import admin
from book.models import BookInfo, PeopleInfo

# Register your models here.

# 注册模型类：在Django管理页面（http://127.0.0.1:8000/admin/ 账号：wyang，密码：123456），
# 将显示出这里注册过实体类，可通过该页面直接对数据库数据进行操作
admin.site.register(BookInfo)
admin.site.register(PeopleInfo)
