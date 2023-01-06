"""
Django settings for server project.

Generated by 'django-admin startproject' using Django 4.1.3.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-p534c)dytyoe#8iy&*+^eabjood90$@qy!uvfoqqvlpj8co4!i"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # 'data.apps.DataConfig',
    'rest_framework',
    'rest_framework.authtoken',
    'corsheaders',
    'djoser',
    'data',
]

CORS_ALLOWED_ORIGINS = [
    "http://localhost:8080",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    'corsheaders.middleware.CorsMiddleware',
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]


# MIDDLEWARE_CLASSES = [
#     'django.middleware.cache.UpdateCacheMiddleware',
#     'django.middleware.common.CommonMiddleware',
#     'django.middleware.cache.FetchFromCacheMiddleware',
# ]

CACHE_TTL = 60 * 1500

CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://127.0.0.1:6379/1",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    }
}

ROOT_URLCONF = "backend.urls"


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
            ],
        },
    },
]

WSGI_APPLICATION = "backend.wsgi.application"

# staging
DATABASES = {
    "default": {
    },
    'auth_db':{
        "NAME": "django",
        "ENGINE": "django.db.backends.mysql",
        "USER": 'django',
        "PASSWORD": "ttd2021!",
        "HOST": "118.69.153.36",
        "PORT": "33064"
    },
    'data_db':{
        "NAME": "ttd_staging_data",
        "ENGINE": "django.db.backends.mysql",
        "USER": 'django',
        "PASSWORD": "ttd2021!",
        "HOST": "118.69.153.36",
        "PORT": "33064"
    },
    'report_db':{
        "NAME": "ttd_staging_report",
        "ENGINE": "django.db.backends.mysql",
        "USER": 'django',
        "PASSWORD": "ttd2021!",
        "HOST": "118.69.153.36",
        "PORT": "33064"
    },
}

# # product
# DATABASES = {
#     "default": {
#     },
#     'auth_db':{
#         "NAME": "ttd",
#         "ENGINE": "django.db.backends.mysql",
#         "USER": 'ttd',
#         "PASSWORD": "ftc2018",
#         "HOST": "captain.app.ftcjsc.com",
#         "PORT": "33064"
#     },
#     'data_db':{
#         "NAME": "ttd_data",
#         "ENGINE": "django.db.backends.mysql",
#         "USER": 'ttd',
#         "PASSWORD": "ftc2018",
#         "HOST": "captain.app.ftcjsc.com",
#         "PORT": "33064"
#     },
#     'report_db':{
#         "NAME": "ttd_report",
#         "ENGINE": "django.db.backends.mysql",
#         "USER": 'ttd',
#         "PASSWORD": "ftc2018",
#         "HOST": "captain.app.ftcjsc.com",
#         "PORT": "33064"
#     },
# }




# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = "/static/"

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
]


# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

DATABASE_ROUTERS = ['routers.db_routers.AuthRouter',
                    'routers.db_routers.DataRouter',
                    'routers.db_routers.ReportRouter'
                    
                    ]


# WEBPACK_LOADER = {
#     'DEFAULT': {
#         'CACHE': not DEBUG,
#         'BUNDLE_DIR_NAME': 'webpack_bundles/',
#         'STATS_FILE': str(BASE_DIR.joinpath('client' ,'webpack-stats.json')),
#         'POLL_INTERVAL' : 0.1,
#         'TIMEOUT': None,
#         'IGNORE' :[r'.+\.hot-update.js' , r'.+\.map'],
#     },
# }