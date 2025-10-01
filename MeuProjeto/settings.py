# settings.py

from pathlib import Path
import os
from dotenv import load_dotenv # <-- 1. IMPORTAMOS A FUNÇÃO

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# 2. CARREGAMOS AS VARIÁVEIS DE AMBIENTE LOGO NO INÍCIO
load_dotenv(os.path.join(BASE_DIR, '.env'))

# ====================================================================
# CONFIGURAÇÕES DE SEGURANÇA
# ====================================================================

# A chave secreta agora é lida DIRETAMENTE do arquivo .env
# Removemos a chave antiga que estava escrita no código.
SECRET_KEY = os.getenv('SECRET_KEY')

# Apenas uma definição para DEBUG e ALLOWED_HOSTS
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
    'tarefas', # Sua aplicação
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
        'PASSWORD': os.getenv('DB_PASSWORD'), # Lê a senha do .env
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

LANGUAGE_CODE = 'pt-br' # Mudado para português do Brasil
TIME_ZONE = 'America/Sao_Paulo' # Mudado para o fuso de São Paulo
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

# Configuração de email para o terminal (ótimo para desenvolvimento)
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'