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

PROJECT_TITLE = "e-Consent for ASAP"
PROJECT_TITLE_LINK = "login_router"
PROJECT_LOGO = "images/asap/logo.jpg"

ACCOUNT_SELF_UNLOCK_ENABLED = True

# Registration customisation (if any) goes here
# REGISTRATION_CLASS = "asap.custom_registration.CustomRegistration"

VERSION = env.get('app_version', '%s (asap)' % asap.VERSION)
