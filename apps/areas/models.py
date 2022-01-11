from django.db import models


# Create your models here.

class Area(models.Model):
    """
    省市区表数据
    """
    name = models.CharField(max_length=20, verbose_name='名称')
    parent = models.ForeignKey('self', on_delete=models.SET_NULL, related_name='subs',
                               null=True, blank=True, verbose_name='上级行政区划')

    """
    related_name：表示关联数据库表的名字，默认为 关联模型类名小写_set（area_set）,
    可以通过修改 related_name 来修改默认的值（subs）
    """

    class Meta:
        db_table = 't_areas'
        verbose_name = '省市区'
        verbose_name_plural = '省市区'

    def __str__(self):
        return self.name
