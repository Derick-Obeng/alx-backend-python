# Test settings for Jenkins pipeline and GitHub Actions
from .settings import *
import os
import sys

# Override database for testing
# Use MySQL in GitHub Actions, SQLite locally
if os.getenv('GITHUB_ACTIONS'):
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': os.getenv('DATABASE_NAME', 'messaging_app_test'),
            'USER': os.getenv('DATABASE_USER', 'messaging_user'),
            'PASSWORD': os.getenv('DATABASE_PASSWORD', 'messaging_password'),
            'HOST': os.getenv('DATABASE_HOST', '127.0.0.1'),
            'PORT': os.getenv('DATABASE_PORT', '3306'),
            'OPTIONS': {
                'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
            },
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': ':memory:',  # Use in-memory database for faster tests
        }
    }

# Disable migrations for faster testing
class DisableMigrations:
    def __contains__(self, item):
        return True
    
    def __getitem__(self, item):
        return None

# Only use this for testing
if 'test' in sys.argv or 'pytest' in sys.modules:
    MIGRATION_MODULES = DisableMigrations()

# Simpler password validation for testing
AUTH_PASSWORD_VALIDATORS = []

# Disable logging during tests
LOGGING_CONFIG = None

# Use console email backend for testing
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
