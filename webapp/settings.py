import os

import dj_database_url

from webapp.settings_social_oauth import SOCIALACCOUNT_PROVIDERS


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

ENVIRONMENT = os.environ.get('ENVIRONMENT')
SECRET_KEY = os.environ.get('SECRET_KEY')
DEBUG = (os.environ.get('DEBUG') == 'True')

# Deployment Web Security
if ENVIRONMENT == 'production':
    DEBUG = (os.environ.get('DEBUG') == 'True')
    ALLOWED_HOSTS = ['django-docker-launchpad.herokuapp.com']
    # Help guard against XSS attacks
    SECURE_BROWSER_XSS_FILTER = True
    # Protection against Clickjacking
    X_FRAME_OPTIONS = 'DENY'
    # Force all non-HTTPS traffic to be redirected to HTTPS
    SECURE_SSL_REDIRECT = True
    # HTTP Strict Transport Security (HSTS)
    # Enforce web browsers should only interact via HTTPS
    SECURE_HSTS_SECONDS = 3600
    SECURE_HSTS_INCLUDE_SUBDOMAINS = True
    SECURE_HSTS_PRELOAD = True  #
    SECURE_CONTENT_TYPE_NOSNIFF = True
    # Force cookies over HTTPS
    SESSION_COOKIE_SECURE = True
    # Force CSRF cookies over HTTPS
    CSRF_COOKIE_SECURE = True
    #
    SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
else:
    ALLOWED_HOSTS = []


INSTALLED_APPS = [
    'rest_framework',
    'rest_framework.authtoken',  # generate tokens on server
    'rest_auth',  # login, logout, password reset endpoints
    'rest_auth.registration',
    'corsheaders',  # corsheaders config

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'whitenoise.runserver_nostatic',  # staticfiles with whitenoise
    'django.contrib.staticfiles',
    'storages',
    'django.contrib.sites',  # allauth config
    'django.contrib.humanize',

    # External
    'crispy_forms',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.github',
    'allauth.socialaccount.providers.linkedin_oauth2',

    # Local
    'users.apps.UsersConfig',
    'pages.apps.PagesConfig',
    'blog.apps.BlogConfig',
]
DEVELOPMENT_INSTALLED_APPS = [
    'debug_toolbar',  # django-debug-toolbar config
    'django_extensions',
]
if ENVIRONMENT == 'development':
    INSTALLED_APPS += DEVELOPMENT_INSTALLED_APPS


MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',  # corsheaders config
    'django.middleware.common.CommonMiddleware',  # corsheaders config

    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # staticfiles with whitenoise
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',  # django-debug-toolbar config
]


ROOT_URLCONF = 'webapp.urls'


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates')
        ],
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


WSGI_APPLICATION = 'webapp.wsgi.application'


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres',
        'USER': 'postgres',
        'PASSWORD': 'postgres',
        'HOST': 'db',
        'PORT': 5432
    }
}


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
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'US/Pacific'
USE_I18N = True
USE_L10N = True
USE_TZ = True


# Assets
STATIC_URL = '/static/'  # URL to reference static files
STATICFILES_DIRS = os.path.join(BASE_DIR, 'assets'),  # Location of static files in local development
STATIC_ROOT = 'staticfiles'  # Location of static files for production
# Make top-down static file search explicit
STATICFILES_FINDERS = [
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
]
MEDIA_URL = '/media/'  # URL we can use in our templates for users' files
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')  # Absolute file system path to user-uploaded files' directory


# User Management
AUTH_USER_MODEL = 'users.CustomUser'  # CustomUser instead of the default User model
LOGIN_REDIRECT_URL = 'home'
# LOGOUT_REDIRECT_URL = 'home'  # not needed if allauth used
ACCOUNT_LOGOUT_REDIRECT = 'home'  # being explicit with allauth logout redirect
SITE_ID = 1
AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
)
ACCOUNT_SESSION_REMEMBER = None  # login Remember Me check box
ACCOUNT_SIGNUP_PASSWORD_ENTER_TWICE = True
ACCOUNT_USERNAME_REQUIRED = True
ACCOUNT_AUTHENTICATION_METHOD = 'username_email'
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_UNIQUE_EMAIL = True

ACCOUNT_LOGIN_ATTEMPTS_LIMIT = 5
ACCOUNT_LOGIN_ATTEMPTS_TIMEOUT = 600

ACCOUNT_LOGOUT_ON_PASSWORD_CHANGE = True
ACCOUNT_LOGIN_ON_PASSWORD_RESET = True


CRISPY_TEMPLATE_PACK = 'bootstrap4'


REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.TokenAuthentication',
    ],
}


# corsheaders config
CORS_ORIGIN_WHITELIST = [
    'http://127.0.0.1:3000',
]
CORS_ALLOW_METHODS = [
    'DELETE',
    'GET',
    'OPTIONS',
    'PATCH',
    'POST',
    'PUT',
]


# SendGrid Email
# Setting EMAIL_BACKEND not necessary for SendGrid
EMAIL_HOST = 'smtp.sendgrid.net'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = os.environ.get('SENDGRID_USERNAME')
EMAIL_HOST_PASSWORD = os.environ.get('SENDGRID_PASSWORD')
# None SendGrid Email Settings
DEFAULT_FROM_EMAIL = 'concierge@djangowebapp.com'


# Stripe Payment
STRIPE_TEST_PUBLISHABLE_KEY = os.environ.get('STRIPE_TEST_PUBLISHABLE_KEY')
STRIPE_TEST_SECRET_KEY = os.environ.get('STRIPE_TEST_SECRET_KEY')


# For django-debug-toolbar
# Get the docker machine IP which web server is running in
# If not running in docker, INTERNAL_IPS = '127.0.0.1'
if ENVIRONMENT == 'development':
    import socket
    hostname, _, ips = socket.gethostbyname_ex(socket.gethostname())
    INTERNAL_IPS = [ip[:-1] + "1" for ip in ips]
    if DEBUG:
        print('Docker machine IP:', INTERNAL_IPS)


# Amazon S3 Credentials and django-storages settings
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'  # upload media files to S3
AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME = os.environ.get('AWS_STORAGE_BUCKET_NAME')
# STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'  # put static files in S3
AWS_S3_FILE_OVERWRITE = False  # prevent overwriting different files with same names
AWS_DEFAULT_ACL = None  # all files will inherit from bucket’s ACL (Access Control List)

# Heroku
if ENVIRONMENT == 'production':
    db_from_env = dj_database_url.config(conn_max_age=500)
    DATABASES['default'].update(db_from_env)
