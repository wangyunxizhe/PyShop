from django.shortcuts import render
from fdfs_client.client import Fdfs_client

# 使用FastDFS上传图片至服务器
# 1，加载FastDFS客户端
client = Fdfs_client('utils/fastdfs/client.conf')
# 2，上传图片
client.upload_by_filename('E:/py-workspaces/pyShop/static/好像一条狗.jpg')
# 3，获取file_id，upload_by_filename上传成功会返回字典数据（其中包含file_id）
