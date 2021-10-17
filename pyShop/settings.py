"""
Django settings for pyShop project.

Generated by 'django-admin startproject' using Django 3.2.2.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""
import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-g@j1popq-6(c_92u9iz%%30irm+v)r^12!yoc_+^85_x@@zpwi'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# 默认访问IP：127.0.0.1，这里设置为 '*'
ALLOWED_HOSTS = ['*']

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
    # 将新建的子应用“book”，注册到项目中。方案1
    # 'book'
    # 方案2
    'book.apps.BookConfig',
    'person.apps.PersonConfig',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    # 如果要禁用session把下面这行注释掉
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    # Django默认会对POST请求进行验证，把这行注释掉就可以取消验证
    # 'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'pyShop.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates']
        ,
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
        # 'PASSWORD': '870814',
        # 'NAME': 'python',
        'PASSWORD': '666666',
        'NAME': 'pyshop',
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
        'LOCATION': 'redis://192.168.112.130:6379/0',
        'OPTIONS': {
            'CLIENT_CLASS': 'django_redis.client.DefaultClient',
        }
    }
}
# 缓存策略：本地缓存，储存在本机内存中，如果丢失则不能找回，比数据库方式更快。将Django默认保存session的数据库指定为Redis
SESSION_ENGINE = 'django.contrib.sessions.backends.cache'
# 缓存策略：混合存储，redis、MySQL都会落库。优先缓存进行存取，如果没有则从数据库存取
# SESSION_ENGINE = 'django.contrib.sessions.backends.cached_db'
# 保存在名为“default”的配置信息中（因为可能有多个配置信息）
SESSION_CACHE_ALIAS = 'default'
# Redis相关配置-end
