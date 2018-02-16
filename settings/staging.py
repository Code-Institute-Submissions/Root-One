from base import *

DEBUG = False

# Database settings

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Paypal Settings
PAYPAL_NOTIFY_URL = 'http://127.0.0.1:8000/project-3-code-inst.herokuapp.com'
PAYPAL_RECEIVER_EMAIL = 'hcuk106_buyer@outlook.com'

SITE_URL = 'https://project-3-code-inst.herokuapp.com'
ALLOWED_HOSTS.append('project-3-code-inst.herokuapp.com')

# Log DEBUG information to the console
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': os.getenv('DJANGO_LOG_LEVEL', 'DEBUG'),
        },
    },
}