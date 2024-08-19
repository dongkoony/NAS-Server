# ./nas_project/settings.py

import os
from pathlib import Path
from dotenv import load_dotenv

# 프로젝트의 루트 디렉토리(BASE_DIR)를 정의합니다.
BASE_DIR = Path(__file__).resolve().parent.parent

# .env 파일 로드
load_dotenv()

# 환경 변수에서 SECRET_KEY 불러오기
SECRET_KEY = os.getenv('DJANGO_SECRET_KEY', 'default-key-if-not-found')

# 디버그 모드 설정
DEBUG = os.getenv('DJANGO_DEBUG', 'False') == 'True'

# 허용된 호스트 설정 (쉼표로 구분된 IP 주소를 리스트로 변환)
ALLOWED_HOSTS = os.getenv('DJANGO_ALLOWED_HOSTS', 'localhost,127.0.0.1').split(',')

# 루트 URL 설정
ROOT_URLCONF = 'nas_project.urls'

# 정적 파일 경로 설정
STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]

# 로그인 및 리디렉션 설정
LOGIN_URL = '/'  # 로그인 페이지로 리디렉션 설정
LOGIN_REDIRECT_URL = '/dashboard/'  # 로그인 성공 후 리디렉션될 페이지

# 설치된 앱들
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'nas_app',  # 사용자 정의 앱
    'django_extensions',  # Django Extensions 추가
]

STATIC_URL = '/static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'nas_app', 'static'),
]

# 템플릿 설정
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

# 미들웨어 설정
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# 데이터베이스
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.getenv('DB_NAME'),
        'USER': os.getenv('DB_USER'),
        'PASSWORD': os.getenv('DB_PASSWORD'),
        'HOST': os.getenv('DB_HOST'),
        'PORT': os.getenv('DB_PORT'),
        'OPTIONS': {
            'unix_socket': '/var/run/mysqld/mysqld.sock',
        }
    }
}

# 기본 자동 필드 설정
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'