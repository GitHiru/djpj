from pathlib import Path
import os #add

BASE_DIR = Path(__file__).resolve().parent.parent

DEBUG = True #edit

ALLOWED_HOSTS = ['*'] #edit

SITE_ID = 1 #add:sitemap

# Application definition
INSTALLED_APPS = [
    'whitenoise.runserver_nostatic', #add:Whitenoise(開発環境でも使用設定)
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'diary.apps.DiaryConfig', #add:myapplication
    'django.contrib.sites', #add:sitemap
    'django.contrib.sitemaps', #add:sitemap
    'storages', #add:aws
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware', #add:Whitenoise
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'djpj.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'diary/templates')], #edit
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'djpj.context_processors.common', #add
            ],
        },
    },
]

# WebServerGatewayInterface
WSGI_APPLICATION = 'djpj.wsgi.application'

# Database
# 🔗https://docs.djangoproject.com/en/3.1/ref/settings/#databases
#edit
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': '',
        'USER': '',
        'PASSWORD': '',
        'HOST': 'host',
        'PORT': '',
    }
}


# Password validation
# 🔗https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators
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
# 🔗https://docs.djangoproject.com/en/3.1/topics/i18n/
LANGUAGE_CODE = 'ja'
TIME_ZONE     = 'Asia/Tokyo'
USE_I18N      = True
USE_L10N      = True
USE_TZ        = True


# Staticfiles (CSS, JavaScript, Images)
# 🔗https://docs.djangoproject.com/en/3.1/howto/static-files/
MEDIA_URL   = '/media/' #メディアファイル配信URL
MEDIA_ROOT  = os.path.join(BASE_DIR, 'staticfiles', 'media_root') #メディアファイルの保存先

STATIC_URL  = '/static/' #静的ファイル配信URL
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles') #collectstatic時の静的ファイル保存先
STATIC_DIRS = [
    os.path.join(BASE_DIR, 'static'),
    ]

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'


# django-herokuの実行を追加 #add
try:
    from .settings_local import *
except ImportError:
    pass

if not DEBUG:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    import django_heroku
    django_heroku.settings(locals())

SECRET_KEY = os.environ.get('SECRET_KEY') #add:test
'''
    # from storages.backends.s3boto3 import S3Boto3Storage
    # def MediaRootS3BotoStorage(): return S3Boto3Storage(location='media')
    # def StaticRootS3BotoStorage(): return S3Boto3Storage(location='static')

    # collectstaic時にS3を使う
    # DEFAULT_FILE_STORAGE = 'MediaRootS3BotoStorage' #ファイルアップロードでS3へ
    DEFAULT_FILE_STORAGE = 'storage.backends.s3boto3.S3Boto3Storage' #ファイルアップロードでS3へ
    # STATICFILES_STORAGE = 'StaticRootS3BotoStorage' #colectstaticでS3へ
    STATICFILES_STORAGE = 'storage.backends.s3boto3.S3Boto3Storage' #ファイルアップロードでS3へ

    AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
    AWS_STORAGE_BUCKET_NAME = os.environ.get('AWS_STORAGE_BUCKET_NAME')

    AWS_S3_FILE_OVERWRITE = False
    AWS_DEFAULT_ACL = None
    AWS_QUERYSTRING_AUTH = False # URLからクエリパラメータを削除
    AWS_PRELOAD_METADATA = True # これをTrueにしたほうがファイル変更のチェックが速くなる
    AWS_S3_OBJECT_PARAMETERS = {
        'CacheControl': 'max-age=86400',  # キャッシュの有効期限（最長期間）= 1日
    }

    # S3バケットのURL（サブドメインのURLを使ってもどちらでも◎）
    AWS_S3_URL = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME
    MEDIA_URL = 'https://%s/%s/' % (AWS_S3_URL, 'media')
    STATIC_URL = 'https://%s/%s/' % (AWS_S3_URL, 'static')
'''


#add: database
import dj_database_url #add
db_from_env = dj_database_url.config(conn_max_age=500, ssl_require=True)
DATABASES['default'].update(db_from_env)
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
