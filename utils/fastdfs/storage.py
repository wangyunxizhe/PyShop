"""
自定义文件存储类
"""
from django.core.files.storage import Storage


class MyStorage(Storage):
    """
    重写Storage中的_open，_save方法，达到返回完整图片网络地址的效果
    """

    def _open(self, name, mode='rb'):
        pass

    def _save(self, name, content, max_length=None):
        pass

    def url(self, name):
        return "http://192.168.68.131:8888/" + name
