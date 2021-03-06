"""
Django settings for pyShop project.

Generated by 'django-admin startproject' using Django 3.2.2.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""
import os
import sys
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
from django.template.backends import django

BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-g@j1popq-6(c_92u9iz%%30irm+v)r^12!yoc_+^85_x@@zpwi'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# 默认访问IP：127.0.0.1，也可设置为 '*'，或指定具体域名（同时更改本地host文件，如Linux中就需要 vim /etc/hosts）
ALLOWED_HOSTS = ['127.0.0.1', 'www.pyshop.site']

# Application definition
# 注册/安装 子应用的配置项
# 一定要注册子应用，如果不注册，在迁移的时候系统检测不到
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # 将新建的子应用“book”，注册到项目中。
    # 方案1：直接写子应用的名字 book
    # 'book'
    # 方案2：写配置类的地址
    'book.apps.BookConfig',
    'person.apps.PersonConfig',
    # 当子应用users与manage.py不同级时注意下面的写法，在apps/users/apps.py中的name = 'apps.users'
    'apps.users',
    'apps.verifications',
    'apps.areas',
    'apps.goods',
    'apps.contents',
    # CORS支持跨域
    'corsheaders',
    # ES支持模块
    'haystack',
    # Linux定时任务支持模块
    'django_crontab',
    # Windows/Linux定时任务支持模块
    'django_apscheduler',
]

# django的中间件
MIDDLEWARE = [
    # CORS的配置要放在中间件的最上面！！！
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    # 如果要禁用session把下面这行注释掉
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    # Django默认会对POST请求进行验证，把这行注释掉就可以取消验证
    # 'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # 注册自定义的django中间件
    'book.middleware.TestMiddleWare',
    'book.middleware.TestMiddleWare2',
]

ROOT_URLCONF = 'pyShop.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'pyShop.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

# Django默认生成，sqlite3数据库
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }
# 将数据库更换为Mysql
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'HOST': '127.0.0.1',
        'PORT': 3306,
        'USER': 'root',
        # 笔记本
        'PASSWORD': '870814',
        'NAME': 'python',
        # 台式机
        # 'PASSWORD': '666666',
        # 'NAME': 'pyshop',
    }
}

# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/
# 设置语言
LANGUAGE_CODE = 'zh-hans'
# 设置时区
TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = False

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'
# 添加项目静态资源存放路径
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Redis相关配置-start（用于保存session）
CACHES = {
    # 如果配置多个，在与‘default’同级增加
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        # 台式机
        # 'LOCATION': 'redis://192.168.112.130:6379/0',
        # 笔记本
        'LOCATION': 'redis://192.168.68.131:6379/0',
        'OPTIONS': {
            'CLIENT_CLASS': 'django_redis.client.DefaultClient',
        }
    },
    'session': {  # 专门用于保存session
        'BACKEND': 'django_redis.cache.RedisCache',
        # 台式机
        # 'LOCATION': 'redis://192.168.112.130:6379/1',
        # 笔记本
        'LOCATION': 'redis://192.168.68.131:6379/1',
        'OPTIONS': {
            'CLIENT_CLASS': 'django_redis.client.DefaultClient',
        }
    },
    'code': {
        'BACKEND': 'django_redis.cache.RedisCache',
        # 台式机
        # 'LOCATION': 'redis://192.168.112.130:6379/2',
        # 笔记本
        'LOCATION': 'redis://192.168.68.131:6379/2',
        'OPTIONS': {
            'CLIENT_CLASS': 'django_redis.client.DefaultClient',
        }
    }
}
# 缓存策略：本地缓存，储存在本机内存中，如果丢失则不能找回，比数据库方式更快。将Django默认保存session的数据库指定为Redis
SESSION_ENGINE = 'django.contrib.sessions.backends.cache'
# 缓存策略：混合存储，redis、MySQL都会落库。优先缓存进行存取，如果没有则从数据库存取
# SESSION_ENGINE = 'django.contrib.sessions.backends.cached_db'
# 保存在名为“session”的配置信息中（因为可能有多个配置信息）。这里使用 1 号库来保存session信息
SESSION_CACHE_ALIAS = 'session'
# Redis相关配置-end

# 日志相关配置
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,  # 是否禁用已经存在的日志器
    'formatters': {  # 日志格式
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(lineno)d %(message)s'
        },
        'simple': {
            'format': '%(levelname)s %(module)s %(lineno)d %(message)s'
        }
    },
    'filters': {  # 对日志进行过滤
        'require_debug_true': {  # django在debug模式下才输出日志
            '()': 'django.utils.log.RequireDebugTrue'
        }
    },
    'handlers': {  # 日志处理方法
        'console': {  # 向终端中输出日志
            'level': 'INFO',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        },
        'file': {  # 向文件中输出日志
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(BASE_DIR, 'logs/all.log'),  # 日志文件位置
            'maxBytes': 300 * 1024 * 1024,
            'backupCount': 10,
            'formatter': 'verbose'
        }
    },
    'loggers': {  # 日志器
        'myLog': {  # 定义一个名为myLog的日志器
            'handlers': ['console', 'file'],  # 同时向终端和文件输出日志
            'propagate': True,  # 是否继续传递日志信息
            'level': 'INFO'  # 日志器接收的最低日志级别
        }
    }
}

# 使用自定义的User覆盖系统自带的User类，做“用户管理”相关功能时使用
# 这个“点式”路径包含Django子应用的名称（必须在INSTALLED_APPS中注册过），以及要用作User模型的自定义模型的名称（项目中正好也叫User）
AUTH_USER_MODEL = 'users.User'

# CORS白名单
CORS_ORIGIN_WHITELIST = (
    'http://127.0.0.1:8080',
    'http://localhost:8080',
)
# 允许携带cookie
CORS_ALLOW_CREDENTIALS = True

#############################邮件功能相关配置###############################
# EMAIL_BACKEND = 'django.core.email.backends.smtp.EmailBackend'
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.163.com'
EMAIL_PORT = 25
EMAIL_HOST_USER = 'wu43456229@163.com'
EMAIL_HOST_PASSWORD = 'ZJVOLVRUGQIYHXSU'
# 收件人看到的发件人
EMAIL_FROM = '蔡徐抻<wu43456229@163.com>'
# 自定义配置
VERIFY_URL = 'http://127.0.0.1:8080/success_verify_email.html'

#############################加载自定义文件存储类############################
# 指定自定义的Django文件存储类
DEFAULT_FILE_STORAGE = 'utils.fastdfs.storage.MyStorage'

#############################ES 相关配置项#################################
HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.elasticsearch_backend.ElasticsearchSearchEngine',
        'URL': 'http://192.168.68.131:9200/',
        'INDEX_NAME': 'wyuan',
    },
}
# 设置搜索 每页返回的记录条数
HAYSTACK_SEARCH_RESULTS_PER_PAGE = 5

#############################定时任务相关配置项################################
# django-crontab配置如下（只支持Linux系统）
CRONJOBS = [
    ('*/1 * * * *', 'utils.crons.generic_shop_index', '>> ' + os.path.join(BASE_DIR, 'logs/crontab.log'))
]
