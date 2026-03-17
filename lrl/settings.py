# import os
# from pathlib import Path
# from dotenv import load_dotenv
# from django.contrib.sites.shortcuts import get_current_site

# BASE_DIR = Path(__file__).resolve().parent.parent
# load_dotenv(BASE_DIR / ".env")
# EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
# EMAIL_HOST = "smtp.gmail.com"
# EMAIL_PORT = 587
# EMAIL_USE_TLS = True
# EMAIL_HOST_USER = "LaddooRaLaheriya@gmail.com"
# EMAIL_HOST_PASSWORD = "qtoe bojj krmr sevi"
# DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
# # settings.py
# ALLOWED_HOSTS = ["127.0.0.1", "localhost"]

# # For building password reset links
# DEFAULT_DOMAIN = "127.0.0.1:8000"

# EMAIL_BACKEND = os.getenv("EMAIL_BACKEND", "django.core.mail.backends.smtp.EmailBackend")
# EMAIL_HOST = os.getenv("EMAIL_HOST", "smtp.gmail.com")
# EMAIL_PORT = int(os.getenv("EMAIL_PORT", "587"))
# EMAIL_USE_TLS = os.getenv("EMAIL_USE_TLS", "True") == "True"
# EMAIL_HOST_USER = os.getenv("EMAIL_HOST_USER")
# EMAIL_HOST_PASSWORD = os.getenv("EMAIL_HOST_PASSWORD")
# DEFAULT_FROM_EMAIL = os.getenv("DEFAULT_FROM_EMAIL", EMAIL_HOST_USER)
# SERVER_EMAIL = os.getenv("SERVER_EMAIL", EMAIL_HOST_USER)
# SERVER_EMAIL = os.getenv("SERVER_EMAIL")
# SECRET_KEY = os.getenv("SECRET_KEY", "dev-secret-key")
# DEBUG = os.getenv("DEBUG", "True") == "True"
# ALLOWED_HOSTS = [h.strip() for h in os.getenv("ALLOWED_HOSTS", "127.0.0.1,localhost").split(",")]
# LOGOUT_REDIRECT_URL = "home"

# INSTALLED_APPS = [
#     'django.contrib.admin',
#     'django.contrib.auth',
#     'django.contrib.contenttypes',
#     'django.contrib.sessions',
#     'django.contrib.messages',
#     'django.contrib.staticfiles',
#     'accounts',
#     'gigs',
#     'cart',
#     'widget_tweaks',
#     'orders',
#     'chatx',
#     "django.contrib.sites",
# ]

# SITE_ID = 1

# MIDDLEWARE = [
#     'django.middleware.security.SecurityMiddleware',
#     'django.contrib.sessions.middleware.SessionMiddleware',
#     'django.middleware.common.CommonMiddleware',
#     'django.middleware.csrf.CsrfViewMiddleware',
#     'django.contrib.auth.middleware.AuthenticationMiddleware',
#     'django.contrib.messages.middleware.MessageMiddleware',
#     'django.middleware.clickjacking.XFrameOptionsMiddleware',
# ]

# ROOT_URLCONF = 'lrl.urls'

# TEMPLATES = [{
#     'BACKEND': 'django.template.backends.django.DjangoTemplates',
#     'DIRS': [BASE_DIR / 'templates'],
#     'APP_DIRS': True,
#     'OPTIONS': {
#         'context_processors': [
#             'django.template.context_processors.debug',
#             'django.template.context_processors.request',
#             'django.contrib.auth.context_processors.auth',
#             'django.contrib.messages.context_processors.messages',
#             'gigs.context_processors.global_data',
#         ],
#     },
# }]

# WSGI_APPLICATION = 'lrl.wsgi.application'

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }

# AUTH_PASSWORD_VALIDATORS = []

# LANGUAGE_CODE = 'en-us'
# TIME_ZONE = 'Asia/Kolkata'
# USE_I18N = True
# USE_TZ = True

# STATIC_URL = '/static/'
# STATICFILES_DIRS = [BASE_DIR / 'static']
# STATIC_ROOT = BASE_DIR / 'staticfiles'

# MEDIA_URL = '/media/'
# MEDIA_ROOT = BASE_DIR / 'media'

# DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
# AUTH_USER_MODEL = 'accounts.User'

# EMAIL_BACKEND = os.getenv("EMAIL_BACKEND", "django.core.mail.backends.console.EmailBackend")
# DEFAULT_FROM_EMAIL = os.getenv("DEFAULT_FROM_EMAIL", "LRL <no-reply@lrl.local>")

# RAZORPAY_KEY_ID = os.getenv("RAZORPAY_KEY_ID", "")
# RAZORPAY_KEY_SECRET = os.getenv("RAZORPAY_KEY_SECRET", "")
# CURRENCY = os.getenv("CURRENCY", "INR")

import os
from pathlib import Path
from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent.parent

# Load environment variables from .env (at project root)
load_dotenv(BASE_DIR / ".env")

# ---------------- Core ----------------
SECRET_KEY = os.getenv("SECRET_KEY", "dev-secret-key")
DEBUG = os.getenv("DEBUG", "True") == "True"
ALLOWED_HOSTS = [h.strip() for h in os.getenv("ALLOWED_HOSTS", "127.0.0.1,localhost").split(",")]

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.sites",   # required for password reset link domains
    # project apps
    "accounts",
    "gigs",
    "cart",
    "orders",
    "chatx",
    "widget_tweaks",
]

SITE_ID = 1

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "lrl.urls"

TEMPLATES = [{
    "BACKEND": "django.template.backends.django.DjangoTemplates",
    "DIRS": [BASE_DIR / "templates"],
    "APP_DIRS": True,
    "OPTIONS": {
        "context_processors": [
            "django.template.context_processors.debug",
            "django.template.context_processors.request",
            "django.contrib.auth.context_processors.auth",
            "django.contrib.messages.context_processors.messages",
            "gigs.context_processors.global_data",
        ],
    },
}]

WSGI_APPLICATION = "lrl.wsgi.application"

# ---------------- Database ----------------
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

# ---------------- Auth ----------------
AUTH_PASSWORD_VALIDATORS = []
AUTH_USER_MODEL = "accounts.User"
LOGOUT_REDIRECT_URL = "home"

# ---------------- I18N/Time ----------------
LANGUAGE_CODE = "en-us"
TIME_ZONE = "Asia/Kolkata"
USE_I18N = True
USE_TZ = True

# ---------------- Static/Media ----------------
STATIC_URL = "/static/"
STATICFILES_DIRS = [BASE_DIR / "static"]
STATIC_ROOT = BASE_DIR / "staticfiles"

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# ---------------- Email (always from .env) ----------------
EMAIL_BACKEND = os.getenv("EMAIL_BACKEND", "django.core.mail.backends.console.EmailBackend")
EMAIL_HOST = os.getenv("EMAIL_HOST", "smtp.gmail.com")
EMAIL_PORT = int(os.getenv("EMAIL_PORT", "587"))
EMAIL_USE_TLS = os.getenv("EMAIL_USE_TLS", "True") == "True"
EMAIL_HOST_USER = os.getenv("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = os.getenv("EMAIL_HOST_PASSWORD")
DEFAULT_FROM_EMAIL = os.getenv("DEFAULT_FROM_EMAIL", EMAIL_HOST_USER)
SERVER_EMAIL = os.getenv("SERVER_EMAIL", EMAIL_HOST_USER)

# For building password reset links locally (plus Sites entry set to same domain)
DEFAULT_DOMAIN = os.getenv("DEFAULT_DOMAIN", "127.0.0.1:8000")

# ---------------- Payments ----------------
RAZORPAY_KEY_ID = os.getenv("RAZORPAY_KEY_ID", "")
RAZORPAY_KEY_SECRET = os.getenv("RAZORPAY_KEY_SECRET", "")
CURRENCY = os.getenv("CURRENCY", "INR")
