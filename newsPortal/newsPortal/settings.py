import os
from pathlib import Path

from django.conf.global_settings import EMAIL_HOST, EMAIL_PORT, EMAIL_HOST_USER, EMAIL_HOST_PASSWORD, EMAIL_USE_SSL, \
    DEFAULT_FROM_EMAIL

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-o9@smb%%dkia+x%w0r)k&blo36#%+(7$9qvs0pi4#t+6xl$(lh'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'news.apps.NewsConfig',
    'django_filters',
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.yandex',  # Провайдер Yandex
    # Другие модули, если есть
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'allauth.account.middleware.AccountMiddleware',
]

ROOT_URLCONF = 'newsPortal.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],  # Убедитесь, что у вас есть папка templates
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

WSGI_APPLICATION = 'newsPortal.wsgi.application'

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Django Allauth settings
AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',  # Конкретный backend для аутентификации
    'allauth.account.auth_backends.AuthenticationBackend',  # Backend Allauth
)

SITE_ID = 1  # Убедитесь, что это соответствует вашему site_id в админке

LOGIN_REDIRECT_URL = '/'  # Направление после входа
LOGOUT_REDIRECT_URL = '/'  # Направление после выхода


# Опциональные настройки Allauth
ACCOUNT_AUTHENTICATION_METHOD = 'username'
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_EMAIL_VERIFICATION = 'optional'
ACCOUNT_UNIQUE_EMAIL = True

# Дополнительные настройки перенаправлений
ACCOUNT_SIGNUP_REDIRECT_URL = '/'  # Направление после регистрации
ACCOUNT_EMAIL_CONFIRMATION_ANONYMOUS_REDIRECT_URL = '/'  # Направление после подтверждения электронной почты
ACCOUNT_LOGOUT_ON_GET = True  # Выход через GET запрос

# Настройки для социальных аккаунтов
SOCIALACCOUNT_PROVIDERS = {
    'yandex': {
        'APP': {
            'client_id': 'YOUR_YANDEX_CLIENT_ID',  # Замените на ваш client_id
            'secret': 'YOUR_YANDEX_CLIENT_SECRET',  # Замените на ваш client_secret
        }
    }
}

ACCOUNT_FORMS = {'signup': 'news.forms.BasicSignupForm'}

EMAIL_HOST = 'smtp.yandex.ru'
EMAIL_PORT = 465
EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD =os.getenv('EMAIL_HOST_PASSWORD')
EMAIL_USE_SSL = True
DEFAULT_FROM_EMAIL = os.getenv('DEFAULT_FROM_EMAIL')



SITE_URL = 'http://127.0.0.1:8000/'

CELERY_BEAT_SCHEDULE = {
    'send_weekly_newsletter': {
        'task': 'your_app.tasks.send_weekly_newsletter',
        'schedule': crontab(hour=8, minute=0, day_of_week=1),
    },
}

CELERY_BROKER_URL = 'redis://localhost:6379/0'
CELERY_RESULT_BACKEND = 'redis://localhost:6379/0'


LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'console': {
            'format': '{asctime} {levelname} {message}',
            'style': '{',
        },
        'console_warning': {
            'format': '{asctime} {levelname} {pathname} {message}',
            'style': '{',
        },
        'console_error': {
            'format': '{asctime} {levelname} {pathname} {message}',
            'style': '{',
        },
        'file_general': {
            'format': '{asctime} {levelname} {module} {message}',
            'style': '{',
        },
        'file_errors': {
            'format': '{asctime} {levelname} {message} {pathname}',
            'style': '{',
        },
        'file_security': {
            'format': '{asctime} {levelname} {module} {message}',
            'style': '{',
        },
        'mail': {
            'format': '{asctime} {levelname} {message} {pathname}',
            'style': '{',
        },
    },
    'filters': {
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse',
        },
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
            'formatter': 'console',
        },
        'console_warning': {
            'level': 'WARNING',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
            'formatter': 'console_warning',
        },
        'console_error': {
            'level': 'ERROR',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
            'formatter': 'console_error',
        },
        'file_general': {
            'level': 'INFO',
            'filters': ['require_debug_false'],
            'class': 'logging.FileHandler',
            'filename': 'general.log',
            'formatter': 'file_general',
        },
        'file_errors': {
            'level': 'ERROR',
            'class': 'logging.FileHandler',
            'filename': 'errors.log',
            'formatter': 'file_errors',
        },
        'file_security': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': 'security.log',
            'formatter': 'file_security',
        },
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler',
            'formatter': 'mail',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console', 'console_warning', 'console_error', 'file_general'],
            'level': 'DEBUG',
        },
        'django.request': {
            'handlers': ['file_errors', 'mail_admins'],
            'level': 'ERROR',
            'propagate': False,
        },
        'django.server': {
            'handlers': ['file_errors', 'mail_admins'],
            'level': 'ERROR',
            'propagate': False,
        },
        'django.template': {
            'handlers': ['file_errors'],
            'level': 'ERROR',
            'propagate': False,
        },
        'django.db.backends': {
            'handlers': ['file_errors'],
            'level': 'ERROR',
            'propagate': False,
        },
        'django.security': {
            'handlers': ['file_security'],
            'level': 'DEBUG',
            'propagate': False,
        },
    },
}
