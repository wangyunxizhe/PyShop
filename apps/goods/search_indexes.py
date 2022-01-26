from haystack import indexes
from apps.goods.models import SKU

"""
1，文件名 search_indexes 是官方文档要求的名字，不能更改。创建的位置是需要检索模型的对应的子应用包中，这样haystack才能检索该模型的数据
2，自定义的索引类必须继承indexes.SearchIndex, indexes.Indexable
3，配置完成后让haystack将数据获取到ES来生成索引（python manage.py rebuild_index）
"""


class SKUIndex(indexes.SearchIndex, indexes.Indexable):
    # 1，每个索引类中都需要有（且只有一个）字段document=True，目的为了向haystack和搜索引擎指示哪个字段是要进行搜索的主要字段
    # 2，use_template=True：允许单独设置一个文件，来指定哪些字段需要检索
    # （这个文件的位置要求：模板文件夹下/search/indexes/子应用名目录/模型类小写_text.txt；见sku_text.txt）
    # 3，text的命令只是惯例，可以随便起
    text = indexes.CharField(document=True, use_template=True)

    # 重写 get_model 方法
    def get_model(self):
        # 返回建立索引的模型类
        return SKU

    # 重写 index_queryset 方法
    def index_queryset(self, using=None):
        # 返回要建立索引的查询结果集
        return SKU.objects.all()
