"""
Django settings for stackopenflow project.

Generated by 'django-admin startproject' using Django 3.2.2.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

import os
from pathlib import Path


def env(name, default=None):
    return os.environ.get(name, default)


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env("SECRET_KEY", "not-so-secret")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env("DJANGO_DEBUG", "0") == "1"

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # 3rd party
    "django_extensions",
    "graphene_django",
    "social_django",
    # stackopenflow
    "stackopenflow.core",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    # "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "stackopenflow.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "stackopenflow.wsgi.application"


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": env("DATABASE_NAME", default="stackopenflow"),
        "USER": env("DATABASE_USER", default="stackopenflow"),
        "PASSWORD": env("DATABASE_PASSWORD", default="stackopenflow"),
        "HOST": env("DATABASE_HOST", default="0.0.0.0"),
        "PORT": env("DATABASE_PORT", default="5432"),
    }
}

# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

validation_pkg = "django.contrib.auth.password_validation"

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": f"{validation_pkg}.UserAttributeSimilarityValidator",
    },
    {
        "NAME": f"{validation_pkg}.MinimumLengthValidator",
    },
    {
        "NAME": f"{validation_pkg}.CommonPasswordValidator",
    },
    {
        "NAME": f"{validation_pkg}.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = "/static/"

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


# =====================================================================================
# Custom Settings
CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_METHODS = ["GET", "POST"]
NODE_DIVIDER = "@"
AUTH_USER_MODEL = "core.User"
FRONTEND_CHOICES = "../stackopenflow-app/src/CHOICES.js"

SOCIAL_AUTH_POSTGRES_JSONFIELD = True
GRAPHENE = {
    "SCHEMA": "stackopenflow.graphql.schema",
    "SCHEMA_OUTPUT": "../stackopenflow-app/schema.json",
    # "MIDDLEWARE": [
    #     "graphql_jwt.middleware.JSONWebTokenMiddleware",
    #     # 'graphene_django.debug.DjangoDebugMiddleware',
    # ],
}
# GRAPHQL_JWT = {
#     "JWT_VERIFY_EXPIRATION": False,
#     # uncomment below lines for enabling time-bound sessions
#     # 'JWT_EXPIRATION_DELTA': timedelta(minutes=60),
#     # 'JWT_REFRESH_EXPIRATION_DELTA': timedelta(days=7),
# }
AUTHENTICATION_BACKENDS = [
    # Mase sure SOCIAL_PROVIDERS has social backend :down:
    "social_core.backends.github.GithubOAuth2",
    # "social_core.backends.twitter.TwitterOAuth",
    # "graphql_jwt.backends.JSONWebTokenBackend",
    "django.contrib.auth.backends.ModelBackend",
]

SOCIAL_PROVIDERS = [
    # should be included in AUTHENTICATION_BACKENDS :top:
    "github",
    # "twitter",
]

# SOCIAL_AUTH_TWITTER_KEY = env("SOCIAL_AUTH_TWITTER_KEY")
# SOCIAL_AUTH_TWITTER_SECRET = env("SOCIAL_AUTH_TWITTER_SECRET")
SOCIAL_AUTH_GITHUB_KEY = env("SOCIAL_AUTH_GITHUB_KEY")
SOCIAL_AUTH_GITHUB_SECRET = env("SOCIAL_AUTH_GITHUB_SECRET")

AWS_ACCESS_KEY_ID = env("AWS_ACCESS_KEY_ID", "minioadmin")
AWS_BUCKET_NAME = env("AWS_BUCKET_NAME", "backend-local")
AWS_BUCKET_REGION = env("AWS_BUCKET_REGION", "ap-south-1")
AWS_EXPIRY = 604700
AWS_S3_ENDPOINT_URL = env("AWS_S3_ENDPOINT_URL")
AWS_SECRET_ACCESS_KEY = env("AWS_SECRET_ACCESS_KEY", "minioadmin")
AWS_REGION = "eu-west-1"

UPLOADS_PREFIX = "uploads"
