from django.apps import AppConfig


class BookConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'book'
    # 添加该属性，在Django管理页面Book对象名将显示为”书籍管理“
    verbose_name = '书籍管理'
