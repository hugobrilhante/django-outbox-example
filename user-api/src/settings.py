"""
Django settings for src project.

Generated by 'django-admin startproject' using Django 3.2.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""
import os
from pathlib import Path

from configurations import Configuration, values


class Base(Configuration):
    # Build paths inside the project like this: BASE_DIR / 'subdir'.

    BASE_DIR = Path(__file__).resolve().parent.parent

    # Quick-start development settings - unsuitable for production
    # See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

    # SECURITY WARNING: keep the secret key used in production secret!
    SECRET_KEY = values.Value()

    # SECURITY WARNING: don't run with debug turned on in production!
    DEBUG = values.BooleanValue(False)

    ALLOWED_HOSTS = values.ListValue([])

    # Application definition

    INSTALLED_APPS = [
        "django.contrib.admin",
        "django.contrib.auth",
        "django.contrib.contenttypes",
        "django.contrib.sessions",
        "django.contrib.messages",
        "django.contrib.staticfiles",
        # App locals
        "src.apps.core.apps.CoreConfig",
    ]

    MIDDLEWARE = [
        "django.middleware.security.SecurityMiddleware",
        "whitenoise.middleware.WhiteNoiseMiddleware",
        "django.contrib.sessions.middleware.SessionMiddleware",
        "django.middleware.common.CommonMiddleware",
        "django.middleware.csrf.CsrfViewMiddleware",
        "django.contrib.auth.middleware.AuthenticationMiddleware",
        "django.contrib.messages.middleware.MessageMiddleware",
        "django.middleware.clickjacking.XFrameOptionsMiddleware",
    ]

    ROOT_URLCONF = "src.urls"

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
                ]
            },
        }
    ]

    WSGI_APPLICATION = "src.wsgi.application"

    # Database
    # https://docs.djangoproject.com/en/3.2/ref/settings/#databases

    DATABASES = values.DatabaseURLValue("sqlite:///" + os.path.join(BASE_DIR, "db.sqlite3"))

    # Password validation
    # https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

    AUTH_PASSWORD_VALIDATORS = [
        {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
        {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
        {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
        {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
    ]

    # Internationalization
    # https://docs.djangoproject.com/en/3.2/topics/i18n/

    LANGUAGE_CODE = values.Value("en-us")

    TIME_ZONE = values.Value("UTC")

    USE_I18N = values.BooleanValue(True)

    USE_L10N = values.BooleanValue(True)

    USE_TZ = values.BooleanValue(True)

    # Static files (CSS, JavaScript, Images)
    # https://docs.djangoproject.com/en/3.2/howto/static-files/

    STATIC_URL = "/static/"

    STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")

    STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

    # See https://docs.djangoproject.com/en/2.2/topics/email/#console-backend
    EMAIL = values.EmailURLValue("console://")

    # Default primary key field type
    # https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

    DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

    AUTH_USER_MODEL = "core.User"


class Dev(Base):
    # See https://docs.djangoproject.com/en/2.2/topics/cache/#dummy-caching-for-development
    CACHES = values.CacheURLValue("dummy://")
    # See http://whitenoise.evans.io/en/stable/django.html#using-whitenoise-in-development
    Base.INSTALLED_APPS.insert(0, "whitenoise.runserver_nostatic")


class Prod(Base):
    pass
