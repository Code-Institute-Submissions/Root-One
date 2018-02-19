from base import *
import dj_database_url

DEBUG = False

# Database settings

DATABASES = {
    'default': dj_database_url.config('CLEARDB_DATABASE_URL')
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
