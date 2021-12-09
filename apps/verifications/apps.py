from django.apps import AppConfig

'''
子应用：图片/短信验证等
'''
class VerificationsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.verifications'
