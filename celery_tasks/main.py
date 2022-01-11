import os
from celery import Celery

'''
~~~启动celery消费者~~~
在虚拟环境下执行命令：
celery -A celery实例的脚本路径 worker -l info
以本工程为例：E:\py-workspaces\pyShop> celery -A celery_tasks.main worker -l info
当消费者在消费时如报错，执行如下命令
1，pip install eventlet
2，通过该命令启动消费者：celery -A celery_tasks.main worker -l info -P eventlet
1-1，pip install gevent
2-1，celery -A celery_tasks.main worker -l info -P gevent
'''

# 为celery的运行，设置Django环境
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pyShop.settings')
# 1，创建celery实例（参数：main设置脚本路径就可以了，脚本路径是唯一的）
app = Celery('celery_tasks')
# 2.设置broker（通过加载配置文件设置broker）
app.config_from_object('celery_tasks.config')
# 3，让Celery自动检测指定包的任务，入参为列表，类容为tasks的路径们
app.autodiscover_tasks(['celery_tasks.sms','celery_tasks.email'])
