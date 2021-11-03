import re

from django.http import JsonResponse
from django.views import View

from apps.users.models import User


class UsernameCountView(View):

    def get(self, request, username):
        # if not re.match('[a-zA-Z0-9_-]{5,20}', username):
        #     return JsonResponse({'code': 200, 'errMsg': '用户名不符合要求'})
        count = User.objects.filter(username=username).count()
        return JsonResponse({'code': 200, 'count': count, 'errMsg': 'OK'})
