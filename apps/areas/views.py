from django.core.cache import cache
from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from django.views import View

from apps.areas.models import Area


class AreaView(View):
    '''
    获取省份数据接口
    '''

    def get(self, request):
        # 先尝试从缓存中读取数据
        province_list = cache.get('province')
        if province_list is None:
            # 查询省份信息
            provinces = Area.objects.filter(parent=None)
            province_list = []
            # 将数据库查询到的数据对象转换成list（dict），以便于返回给前端的json格式转换
            for province in provinces:
                province_list.append({
                    "id": province.id,
                    "name": province.name
                })
            # 将数据缓存（使用django自带工具缓存进redis）过期时长为1天
            cache.set('province', province_list, 24 * 3600)
        return JsonResponse({'code': 0, 'errmsg': 'ok', 'province_list': province_list})


class SubAreaView(View):
    '''
    获取市，区级联数据
    '''

    def get(self, request, id):
        # 先尝试从缓存中读取数据
        data_list = cache.get('city:%s'%id)
        if data_list is None:
            up_level = Area.objects.get(id=id)
            down_level = up_level.subs.all()
            data_list = []
            for item in down_level:
                data_list.append({
                    "id": item.id,
                    "name": item.name
                })
            # 将数据缓存（使用django自带工具缓存进redis）过期时长为1天
            cache.set('city:%s'%id, data_list, 24 * 3600)
        return JsonResponse({'code': 0, 'errmsg': 'ok', 'sub_data': {'subs': data_list}})
