"""
Django settings for P2PADM project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

print BASE_DIR

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '8tnb^6lw#8r0&=x^@bnkye@4e*^n40&-30dvx^yy_2lr6gmkc3'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'P2PADM.apps.P2Padmin',
    'P2PADM.apps.getP2PInfo_cron'
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
#    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'P2PADM.urls'

WSGI_APPLICATION = 'P2PADM.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/


TEMPLATE_DIRS = (
    os.path.join(os.path.dirname(__file__), 'templates').replace('\\','/'),
)



STATIC_URL = '/static/'

STATIC_ROOT = os.path.join(os.path.dirname(__file__),'static')

STATICFILES_DIRS = (
#    ('dashboard.css',os.path.join(STATIC_ROOT,'/')),  
#    ('dashboard.css',STATIC_ROOT),
    ('Chart.js-master',os.path.join(STATIC_ROOT,'Chart.js-master').replace('\\','/') ),  
    ('css',os.path.join(STATIC_ROOT,'css').replace('\\','/') ),  
    ('js',os.path.join(STATIC_ROOT,'js').replace('\\','/') ), 
    ('images',os.path.join(STATIC_ROOT,'images').replace('\\','/') ), 
    ('upload',os.path.join(STATIC_ROOT,'upload').replace('\\','/') ), 
)
