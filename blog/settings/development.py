import os
import mimetypes
mimetypes.add_type("text/css", ".css", True)
mimetypes.add_type("text/html", ".html", True)
mimetypes.add_type("text/html", ".js", True)
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '&49ga4rqxrp)^w=%ed&s4qf0*)1yvl!$6j=e@b^^e=i-s3g+@+'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True


ALLOWED_HOSTS = []

if DEBUG:
    # durin devolopment only batuhan
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    "article",
    'crispy_forms',
    "ckeditor",
    'ckeditor_uploader',
    'django_cleanup',
    "account",
    "news",
    "interviews",
    'django_email_verification',
    'journals',
    'django_social_share'


]
CKEDITOR_UPLOAD_PATH = 'uploads/'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'blog.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ["templates"],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.media',
            ],
        },
    },
]

WSGI_APPLICATION = 'blog.wsgi.application'


SESSION_COOKIE_AGE = 60 * 60 * 24 * 30  # One month

# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': 'ejournal',
#         'USER' : 'postgres',
#         'PASSWORD': '12345678',
#         'HOST': 'localhost',
#         'PORT': '5432',
#     }
# }
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': os.environ['DBNAME'],
#         'HOST': os.environ['DBHOST'],
#         'USER': os.environ['DBUSER'],
#         'PASSWORD': os.environ['DBPASS'] 
#     }
# }
hostname = os.environ['DBHOST']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ['DBNAME'],
        'HOST': hostname + ".postgres.database.azure.com",
        'USER': os.environ['DBUSER'],
        'PASSWORD': os.environ['DBPASS'] 
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

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


AUTH_USER_MODEL = 'account.Account'

# Internationalization
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'tr'

TIME_ZONE = 'Europe/Istanbul'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")

CRISPY_TEMPLATE_PACK = 'bootstrap4'

CKEDITOR_CONFIGS = {
    "default": {
        "removePlugins": "stylesheetparser",
        "allowedContent": True,
        "width": "100%",
        "toolbar": "full",
        "extraPlugins": "codesnippet",
        "extraPlugins": "html5video"
    }
}
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
MAILER_EMAIL_BACKEND = EMAIL_BACKEND
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'djangodeneme77@gmail.com'
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
EMAIL_HOST_PASSWORD = 'asdwer147'