import os
from pathlib import Path
# import psycopg2
# from decouple import config
from dotenv import load_dotenv
load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'bs3$b(+5vqe(=#+5-#p0v6fz9_d)creqg-1ql7exyn18&yx=cu'

DEBUG = True

ALLOWED_HOSTS = ['*','3.108.234.18','172.31.6.103','http://www.tangosixoclock.in','www.tangosixoclock.in','http://tangosixoclock.in','https://www.tangosixoclock.in','tangosixoclock.in','https://tangosixoclock.in']

INSTALLED_APPS = [
    'whitenoise.runserver_nostatic',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'tango',
    'captcha',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'allauth.account.middleware.AccountMiddleware',
]

ROOT_URLCONF = 'Tsoc.urls'


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,'tango/templates')],
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

WSGI_APPLICATION = 'Tsoc.wsgi.application'

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': 'delta',
#         'USER': 'tango',
#         'PASSWORD': 'Django123',
#         'HOST': 'delta.cpzckj1ocmci.ap-south-1.rds.amazonaws.com',
#         'PORT': '5432',
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

STATIC_URL = 'static/'

STATIC_ROOT = os.path.join(BASE_DIR,'staticfiles')

STATICFILES_DIRS = [os.path.join(BASE_DIR,'static')]

MEDIA_URL = '/images/'

MEDIA_ROOT = os.path.join(BASE_DIR,"static/images/")



DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'  
EMAIL_PORT = 587  
EMAIL_USE_TLS = True 

EMAIL_HOST_USER = 'tangosixoclock@gmail.com'
EMAIL_HOST_PASSWORD = 'qlpe ihcc juvi fomm'

DEFAULT_FROM_EMAIL = 'tangosixoclock@gmail.com'

EMAIL_TIMEOUT = 1

# APPEND_SLASH = False

# test payment api
KEY_ID = 'rzp_test_F8MIMQQ24shScO'
KEY_SECRET = 'RF8VtlBN01wRgcOTnO6OqUnL'

# live payment api
# KEY_ID = 'rzp_live_0JNj8abM7pJbL3'
# KEY_SECRET = 'xH8MJ0DQ7GwYZ6z0zLdK7JY5'

