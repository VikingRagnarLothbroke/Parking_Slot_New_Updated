"""
Django settings for car_parking project.

Generated by 'django-admin startproject' using Django 4.2.5.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path
import os
import dj_database_url

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get("SECRET_KEY")

#SECRET_KEY = 'django-insecure-q(n%+41+-6edc&8szsmg^i-m9yr+-4+426!z!&(9xq=!x4(25r'

#'django-insecure-q(n%+41+-6edc&8szsmg^i-m9yr+-4+426!z!&(9xq=!x4(25r'
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get("DEBUG","False").lower() == "true"

#DEBUG= True

ALLOWED_HOSTS = os.environ.get("ALLOWED_HOSTS").split(" ")

#ALLOWED_HOSTS=[]

# Application definition

INSTALLED_APPS = [
    'jazzmin',
    #'livereload',
    'import_export',
    'django_admin_logs',
    'Home.apps.HomeConfig',
    'accounts.apps.AccountsConfig',
    'slots.apps.SlotsConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
DJANGO_ADMIN_LOGS_ENABLED = True

DJANGO_ADMIN_LOGS_DELETABLE = False

JAZZMIN_SETTINGS = {
    "changeform_format": "carousel",
    "site_title": " Admin Login",
    "site_header": "Welcome to admin site",
    "site_logo":"PRFT-img-logo.png",
    "site_brand": "Admin Login",
    "login_logo_dark": True,
    "site_logo_classes": "img-circle",
    "site_icon": None,
    "welcome_sign": "Welcome to the Admin Login",
    "copyright": "Admin Login Ltd",
    "show_ui_builder": True,
}
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    #'livereload.middleware.LiveReloadScript',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'car_parking.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,'template1')],
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

WSGI_APPLICATION = 'car_parking.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'new_one',
        'USER':'postgres',
        'PASSWORD':'Vinay5@reddy',
        'HOST':'localhost'
    }
}

database_url=os.environ.get("DATABASE_URL")
DATABASES['default']=dj_database_url.parse(database_url)

#DATABASES['default']=dj_database_url.parse("postgres://dep_2_user:jNmVEvoAz5kbgS4T8YlISif4wtxqzvyG@dpg-ckjagqglk5ic73dnee3g-a.oregon-postgres.render.com/dep_2")

#postgres://dep_2_user:jNmVEvoAz5kbgS4T8YlISif4wtxqzvyG@dpg-ckjagqglk5ic73dnee3g-a.oregon-postgres.render.com/dep_2
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

TIME_ZONE = 'Asia/Kolkata'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'

STATICFILES_DIRS=[
    os.path.join(BASE_DIR,'static')
]
STATIC_ROOT=os.path.join(BASE_DIR,'assets')
# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'vinay5kumarreddynla@gmail.com'
EMAIL_HOST_PASSWORD = 'xaeg btky rpia otvb'
