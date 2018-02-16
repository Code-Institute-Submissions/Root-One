from base import *

DEBUG = True

INSTALLED_APPS.append('debug_toolbar')

# Database settings

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# paypal settings

SITE_URL = 'http://127.0.0.1:8000'
PAYPAL_NOTIFY_URL = 'http://127.0.0.1:8000/a-specific-url-for-payments'
PAYPAL_RECEIVER_EMAIL = 'hcuk106_buyer@outlook.com'