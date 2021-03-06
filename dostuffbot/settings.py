import os
import env

from django.utils.translation import ugettext_lazy as _

DEBUG = True

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

INSTALLED_APPS = (
    'main',
    'member',
)

LANGUAGES = (
    ('en', _('English')),
    ('fr', _('French')),
    ('ru', _('Russian')),
)
LANGUAGE_CODE = 'en'
LOCALE_PATHS = (
    os.path.join(BASE_DIR, 'locale'),
)

SECRET_KEY = env.SECRET_KEY

MAIN_BOT_NAME = 'Dostuffbot'
SUPPORT_BOT_NAME = 'Dostuffsupportbot'
BOT_CALL_PREFIX = 'bot_'
BOT_ID_REGEX = BOT_CALL_PREFIX + r'(\d*)__.*'
DEFAULT_HANDLER_GROUP = 0
ADMIN_HANDLER_GROUP = 1
MAX_MEMBER_COMMANDS = 10
