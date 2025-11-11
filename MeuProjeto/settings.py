# settings.py

from pathlib import Path
import os
from dotenv import load_dotenv 


BASE_DIR = Path(__file__).resolve().parent.parent

load_dotenv(os.path.join(BASE_DIR, '.env'))

# ====================================================================
# CONFIGURAÇÕES DE SEGURANÇA
# ====================================================================

SECRET_KEY = os.getenv('SECRET_KEY')

DEBUG = True
ALLOWED_HOSTS = []


# ====================================================================
# APLICAÇÕES E MIDDLEWARE
# ====================================================================

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'tarefas', 
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'MeuProjeto.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'MeuProjeto.wsgi.application'


# ====================================================================
# BANCO DE DADOS (DATABASE)
# ====================================================================

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'tasko_db',
        'USER': 'root',
        'PASSWORD': '@Vitinho9392',  # use a MESMA senha que funciona no Workbench
        'HOST': 'localhost',
        'PORT': '3306',
    }
}



# ====================================================================
# VALIDAÇÃO DE SENHAS E INTERNACIONALIZAÇÃO
# ====================================================================

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',},
]

LANGUAGE_CODE = 'pt-br' 
TIME_ZONE = 'America/Sao_Paulo' 
USE_I18N = True
USE_TZ = True


# ====================================================================
# ARQUIVOS ESTÁTICOS (STATIC FILES)
# ====================================================================

STATIC_URL = 'static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
]


# ====================================================================
# OUTRAS CONFIGURAÇÕES
# ====================================================================

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Configuração de email para o terminal 
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'