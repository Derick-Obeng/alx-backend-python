# Test settings for Jenkins pipeline
from .settings import *
import os
import sys

# Override database for testing
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
