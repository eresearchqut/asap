# flake8: noqa
import os

from rdrf.settings import *
import asap


FALLBACK_REGISTRY_CODE = "asap"
LOCALE_PATHS = env.getlist("locale_paths", ['/data/translations/locale'])

# Adding this project's app first, so that its templates overrides base templates
INSTALLED_APPS = [
    FALLBACK_REGISTRY_CODE,
] + INSTALLED_APPS

ROOT_URLCONF = '%s.urls' % FALLBACK_REGISTRY_CODE

SEND_ACTIVATION_EMAIL = False

PROJECT_TITLE = "eConsent Demo"
PROJECT_TITLE_LINK = "login_router"

ACCOUNT_SELF_UNLOCK_ENABLED = True

# Registration customisation (if any) goes here
# REGISTRATION_CLASS = "asap.custom_registration.CustomRegistration"

VERSION = env.get('app_version', '%s (asap)' % asap.VERSION)

LOGIN_FAILURE_LIMIT = 0

CSP_FRAME_SRC = ["'self'", "https://www.youtube.com"]
