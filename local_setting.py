# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-j!&=3&3o717j*-yinwss8nh*rotosua+l0bu9y62@=fn_fd(5d'

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'heroes_villians_database',
        'HOST': 'localhost',
        'USER': 'root',
        'PASSWORD': 'password'


    }
}