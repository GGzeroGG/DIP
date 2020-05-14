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
    'products.apps.ProductsConfig',
    'poster.apps.PosterConfig',
    'manufacture.apps.ManufactureConfig',
    'comments.apps.CommentsConfig',
    'basket.apps.BasketConfig', # Добавление товаров в коризну
    'order.apps.OrderConfig', # Создание заказов
    'authorization.apps.AuthorizationConfig',
    'account.apps.AccountConfig',  # Приложение отвечающее запрофиль пользователя
    'search.apps.SearchConfig',  # Приложение отвечающее за поиск товаров
    
    'social_django', #!!!! УСАНОВИ ЭТО
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware', #!!!! УСАНОВИ ЭТО
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
                'basket.utils.get_basket_item', # Контекст для корзины
                'catalog.utils.menu',  # Контекст для работы меню, с категориями
            ],
        },
    },
]

WSGI_APPLICATION = 'REARMDEVICE.wsgi.application'


# Database
# https://docs.djangoproject.com/en/dev/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
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

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),  # Путь к статичным файлам главных шаблонов
]

MEDIA_URL = '/media/'  # Url путь к медиа фаилам
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')  # Путь к медиа фаилам (для сервера)

LOGIN_URL = '/authorization/login/google-oauth2/'
LOGIN_REDIRECT_URL = "account:account"
LOGOUT_REDIRECT_URL = '/'


ADMIN_MEDIA_PREFIX = '/static/admin/'

#AWS_ACCESS_KEY_ID=AKIAIGRQN2X2MUOND3QA AWS_SECRET_ACCESS_KEY=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

#Для авторизации Google
AUTHENTICATION_BACKENDS = (
    'social_core.backends.google.GoogleOAuth2',
    'django.contrib.auth.backends.ModelBackend',
)

SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = '1063857018477-uol3kogtnlrjlp0okp9jji14jh1ul8kt.apps.googleusercontent.com' # Google Consumer Key
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = '35-zqovMG1SqMcaIeQMGpS2R' # Google Consumer Secret

SOCIAL_AUTH_URL_NAMESPACE = 'social'


import dj_database_url
db_from_env = dj_database_url.config()
DATABASES['default'].update(db_from_env)