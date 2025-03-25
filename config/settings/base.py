import os
import environ
from pathlib import Path

# 根目錄設定
BASE_DIR = Path(__file__).resolve().parent.parent.parent

# 初始化 django-environ
env = environ.Env()
environ.Env.read_env(os.path.join(BASE_DIR, ".env"))

# 安全性相關
SECRET_KEY = env("SECRET_KEY", default="unsafe-default-key-for-dev-only")
DEBUG = env.bool("DEBUG", default=True)

ALLOWED_HOSTS = ["*"]  # 開發階段開放所有來源

# 安裝 App
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    # 第三方套件
    "rest_framework",

    # 你的 App
    "conversation",
    "django.contrib.sites",        

    "allauth",
    "allauth.account",
    "allauth.socialaccount",
]

# Middleware 設定
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "allauth.account.middleware.AccountMiddleware",
]

ROOT_URLCONF = "config.urls"

# Templates 設定
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        # "DIRS": [],
        'DIRS': [BASE_DIR / "templates"],
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

WSGI_APPLICATION = "config.wsgi.application"

# 資料庫設定（PostgreSQL）
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": env("POSTGRES_DB", default="maiagent_db"),
        "USER": env("POSTGRES_USER", default="maiagent_user"),
        "PASSWORD": env("POSTGRES_PASSWORD", default="maiagent_pass"),
        "HOST": env("POSTGRES_HOST", default="localhost"),
        "PORT": env("POSTGRES_PORT", default="5432"),
    }
}

# 密碼驗證
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

# 國際化
LANGUAGE_CODE = "en-us"
TIME_ZONE = "Asia/Taipei"
USE_I18N = True
USE_L10N = True
USE_TZ = True

# 靜態檔案
STATIC_URL = "/static/"
STATIC_ROOT = os.path.join(BASE_DIR, "static")

# 預設主鍵類型
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

ADMIN_URL = "admin/"
SITE_ID = 1
