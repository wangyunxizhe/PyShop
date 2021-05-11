from django.db import models

# Create your models here.
"""
1，自定义的Model类需要继承models.Model，才能跟数据库进行交互映射。
2，继承后，系统会自动为Model类添加一个主键（id）。
3，所有定义的模型类都要在 admin.py 中进行注册
"""


class BookInfo(models.Model):
    # 相当于表的name列中定义了 varchar（10），CharField必须设置max_length，verbose_name属性为Django管理页面专用
    name = models.CharField(max_length=10, unique=True, verbose_name='名字')
    pub_date = models.DateField(null=True)
    read_count = models.IntegerField(default=0)
    comment_count = models.IntegerField(default=0)
    is_del = models.BooleanField(default=False)

    # 设置表名的固定写法
    class Meta:
        db_table = 't_book_info'
        verbose_name = '书本信息'  # verbose_name属性为Django管理页面专用

    def __str__(self):
        return self.name


class PeopleInfo(models.Model):
    # 为性别字段创建一个元组
    GENDER_CHOICE = ((1, '男'), (2, '女'))

    name = models.CharField(max_length=10, unique=True)
    gender = models.SmallIntegerField(choices=GENDER_CHOICE, default=1)
    description = models.CharField(max_length=100, null=True)
    is_del = models.BooleanField(default=False)

    class Meta:
        db_table = 't_people_info'
        verbose_name = '角色信息'

    def __str__(self):
        return self.name

    # 添加外键：角色属于哪本书。并设置为级联删除
    book = models.ForeignKey(BookInfo, on_delete=models.CASCADE)
