from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent.parent


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-os!_z_q7!fy9i=2zl7rm5ld^eyku@1^(g*%%k77x2c2kz(_6#v"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ["localhost", ".vercel.app", ".now.sh"]


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "blog",
    "newsletter",
    "django_filters",
    "widget_tweaks",
    'django.contrib.sites',
    "django.contrib.sitemaps",
    "phonenumber_field",
    "django_htmx",
    # 'django_extensions',
]

SITE_ID = 1

MIDDLEWARE = [
    "django.middleware.common.BrokenLinkEmailsMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    
    "django_htmx.middleware.HtmxMiddleware",
]

ROOT_URLCONF = "DjangoApp.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                
                "blog.context_processors.blog",
                "newsletter.context_processors.newsletter",
            ],
        },
    },
]

WSGI_APPLICATION = "DjangoApp.wsgi.application"


# Password validation

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

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)

STATIC_URL = 'static/'

STATICFILES_DIRS = [
  BASE_DIR / "static",
  BASE_DIR / "media",
]

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles_build', 'static')


MEDIA_URL = '/media/'

MEDIA_ROOT = BASE_DIR / 'media/'

# Default primary key field type

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

API_KEY = "1d588b386cc849c6bdd931ec956169dd"
# API_KEY = "f30ec2d72896462499c31eb735920dd9"

ADMINS = [
    ("Oseni", "marketinsider@zohomail.com"), 
    ("Oseni03", "pysite.03@gmail.com")
]
MANAGERS = ["marketinsider@zohomail.com", "pysite.03@gmail.com"]

DEFAULT_FROM_EMAIL = "marketinsider@zohomail.com"
