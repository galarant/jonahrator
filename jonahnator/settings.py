# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
SECRET_KEY = 'mnazx9ec_rf*7+7#(t&vle7$9jm#x3tzdj4q=0kj^exi9g_qp5'

DEBUG = True
TEMPLATE_DEBUG = True
ALLOWED_HOSTS = []


INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'jonahnator',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'jonahnator.urls'

WSGI_APPLICATION = 'jonahnator.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_TZ = True

USE_I18N = True
USE_L10N = True

STATIC_URL = '/static/'
TEMPLATE_DIRS = (os.path.join(BASE_DIR, 'frontend/app'),)
STATICFILES_DIRS = (os.path.join(BASE_DIR, 'frontend/dist'),)
