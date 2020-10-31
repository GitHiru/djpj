from pathlib import Path
import os #add

BASE_DIR = Path(__file__).resolve().parent.parent

DEBUG = False #edit

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
                'djpj.context_processors.common', #add:djpj/context_processors.py
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
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles') #collectstatic時の静的ファイル保存先
STATIC_URL  = '/static/' #静的ファイル配信URL
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
    )
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

MEDIA_ROOT  = os.path.join(BASE_DIR, 'staticfiles', 'media_root') #メディアファイルの保存先


# 本番とローカルの切替 #add:django-heroku
try:
    from .settings_local import *
except ImportError:
    pass

SECRET_KEY = os.environ.get('SECRET_KEY')

if not DEBUG:
    import django_heroku
    django_heroku.settings(locals())

#add:AWS S3 ローカルでもS3使用
# from djpj.aws.conf import *

MEDIA_URL   = '/media/' #メディアファイル配信URL

#add: database
import dj_database_url #add
db_from_env = dj_database_url.config(conn_max_age=500, ssl_require=True)
DATABASES['default'].update(db_from_env)


# SSL #add:original-domain
# CORS_REPLACE_HTTPS_REFERER = True
# HOST_SCHEME = "https://"
# SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
# SECURE_SSL_REDIRECT = True
# SESSION_COOKIE_SECURE = True
# CSRF_COOKIE_SECURE = True
# SECURE_HSTS_INCLUDE_SUBDOMAINS = True
# SECURE_HSTS_SECONDS = 1000000
# SECURE_FRAME_DENY = True
