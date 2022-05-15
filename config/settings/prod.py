from config.settings.base import *

DEBUG = False

ALLOWED_HOSTS = [env('ALLOWED_HOSTS')]

DATABASES = {
 'default': {
     'ENGINE': 'django.db.backends.sqlite3',
     'NAME': BASE_DIR / 'db.sqlite3',
 }
}

STATIC_ROOT = os.path.join(BASE_DIR, 'static')
