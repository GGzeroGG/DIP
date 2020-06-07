"""
Django settings for REARMDEVICE project.

Generated by 'django-admin startproject' using Django 3.1.dev20200118190725.

For more information on this file, see
https://docs.djangoproject.com/en/dev/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/dev/ref/settings/
"""
import os


from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve(strict=True).parents[1]


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/dev/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'ry0l^uth+7%^#tbt!=v3894s8jttjz79yq20nle4*&c%_dl1r#'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

#DEBUG = bool(os.environ.get('DJANGO_DEBUG', ''))
#TEMPLATE_DEBUG = DEBUG

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_cleanup',  # Подключаемая библиотека котороя удаляет фаилы при удалении родительской модели
    'common.apps.CommonConfig',
    'catalog.apps.CatalogConfig',
    'poster.apps.PosterConfig',
    'comments.apps.CommentsConfig',
    'basket.apps.BasketConfig', # Добавление товаров в коризну
    'authorization.apps.AuthorizationConfig',
    'account.apps.AccountConfig',  # Приложение отвечающее запрофиль пользователя
    'social_django',
    'storages',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'REARMDEVICE.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                
                'basket.utils.get_basket_item',  # Контекст для корзины
            ],
        },
    },
]

WSGI_APPLICATION = 'REARMDEVICE.wsgi.application'


# Database
# https://docs.djangoproject.com/en/dev/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'd3rbmqgk6k6eqm',
        'USER': 'xnghrhhzrtkusp',
        'PASSWORD': '7d0b591b4702f181fc3d978977c4a0699d7f01f77ec7c95eafda192481ab78be',
        'HOST': 'ec2-34-232-147-86.compute-1.amazonaws.com',
        'PORT': '5432',
        'URL': 'postgres://xnghrhhzrtkusp:7d0b591b4702f181fc3d978977c4a0699d7f01f77ec7c95eafda192481ab78be@ec2-34-232-147-86.compute-1.amazonaws.com:5432/d3rbmqgk6k6eqm',
#        'ENGINE': 'django.db.backends.sqlite3',
#        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/dev/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/dev/topics/i18n/

LANGUAGE_CODE = 'ru'

TIME_ZONE = 'Europe/Moscow'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/dev/howto/static-files/

AWS_STORAGE_BUCKET_NAME = os.environ['rearmdevice']                          
MEDIA_ROOT = '/media/'                                                          
S3_URL = 'http://%s.s3.amazonaws.com/' % AWS_STORAGE_BUCKET_NAME                
MEDIA_URL = S3_URL + MEDIA_ROOT                                                 
DEFAULT_FILE_STORAGE = 'REARMDEVICE.s3utils.MediaRootS3BotoStorage'                 
STATICFILES_STORAGE = 'REARMDEVICE.s3utils.StaticRootS3BotoStorage'                 
AWS_ACCESS_KEY_ID = os.environ['AKIAI7GGMOVGWGDO77LA']                             
AWS_SECRET_ACCESS_KEY = os.environ['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']  


STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),  # Путь к статичным файлам главных шаблонов
]

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')  # Путь к медиа фаилам (для сервера)




LOGIN_URL = '/authorization/login/google-oauth2/'
LOGIN_REDIRECT_URL = "account:account"
LOGOUT_REDIRECT_URL = '/'


#Для авторизации Google
AUTHENTICATION_BACKENDS = (
    'social_core.backends.google.GoogleOAuth2',
    'django.contrib.auth.backends.ModelBackend',
)

SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = '1063857018477-uol3kogtnlrjlp0okp9jji14jh1ul8kt.apps.googleusercontent.com' # Google Consumer Key
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = '35-zqovMG1SqMcaIeQMGpS2R' # Google Consumer Secret

SOCIAL_AUTH_URL_NAMESPACE = 'social'

ROBOKASSA_TEST_MODE = True

ROBOKASSA_LOGIN = "RearmDevice"
#ROBOKASSA_PASSWORD1 = "GSKQkhfqR8mQnI35u31P"
#ROBOKASSA_PASSWORD2 = "l3Bf0lwY6SJOkMGv25ow"

ROBOKASSA_ORDER_MODEL = "Rearmdevice.basket.Order"
#ROBOKASSA_SUCCESS_TEMPLATE = "success.html"
#ROBOKASSA_FAIL_TEMPLATE = "fail.html"

#Для тестов
ROBOKASSA_PASSWORD1 = "ymw3de7YeXwAdf7I02BY"
ROBOKASSA_PASSWORD2 = "OEYZMbsQhiXU5Qy184B1"


import dj_database_url
db_from_env = dj_database_url.config()
DATABASES['default'].update(db_from_env)
