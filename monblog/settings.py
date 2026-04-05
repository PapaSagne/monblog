
from pathlib import Path

# BASE_DIR = le dossier racine du projet (là où se trouve manage.py)
BASE_DIR = Path(__file__).resolve().parent.parent

# Clé secrète de sécurité (ne jamais partager en production)
SECRET_KEY = 'django-insecure-monblog-cle-secrete-pour-le-developpement'

# Mode debug : True = affiche les erreurs détaillées (désactiver en production)
DEBUG = True

# Hôtes autorisés à accéder au site
ALLOWED_HOSTS = ['*']

# Applications installées dans le projet
INSTALLED_APPS = [
    'django.contrib.admin',        # Interface d'administration
    'django.contrib.auth',         # Système de connexion/déconnexion
    'django.contrib.contenttypes', # Types de contenu génériques
    'django.contrib.sessions',     # Gestion des sessions utilisateurs
    'django.contrib.messages',     # Messages flash (succès, erreurs...)
    'django.contrib.staticfiles',  # Gestion des fichiers CSS/JS/images
    'blog',                        # Notre application blog
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

ROOT_URLCONF = 'monblog.urls'

# Configuration des templates HTML
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # Django cherchera les templates dans le dossier "templates" à la racine
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                # Permet d'utiliser MEDIA_URL dans les templates
                'django.template.context_processors.media',
            ],
        },
    },
]

WSGI_APPLICATION = 'monblog.wsgi.application'

# Base de données SQLite (simple, parfaite pour le développement)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# Langue française et fuseau horaire de Dakar
LANGUAGE_CODE = 'fr-fr'
TIME_ZONE = 'Africa/Dakar'
USE_I18N = True
USE_TZ = True

# -------------------------------------------------------
# FICHIERS STATIQUES (CSS, JavaScript, images de design)
# STATIC_URL    : l'URL pour accéder aux fichiers statiques
# STATICFILES_DIRS : où Django cherche les fichiers statiques
# -------------------------------------------------------
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static']

# -------------------------------------------------------
# FICHIERS MÉDIAS (images uploadées par l'utilisateur)
# MEDIA_URL  : l'URL pour accéder aux images uploadées
# MEDIA_ROOT : le dossier où Django stocke les images uploadées
# -------------------------------------------------------
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'