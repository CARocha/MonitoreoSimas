# Django settings for Monitoreo project.

from local_settings import *

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale
USE_L10N = True

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = PROJECT_DIR + '/media'

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = '/archivos/'

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = '/static/'

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'o7l3pco1d#9%uxwj_36kd@xq)m3_rli6$-l5-h!iev4p23mt*='

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

ROOT_URLCONF = 'monitoreo.urls'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    PROJECT_DIR + '/templates',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.contrib.auth.context_processors.auth',
    'django.contrib.messages.context_processors.messages',
    'django.core.context_processors.request',
    #'pagination.middleware.PaginationMiddleware',
)

INSTALLED_APPS = (
   # 'admin_tools',
   # 'admin_tools.theming',
   # 'admin_tools.menu',
   # 'admin_tools.dashboard',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    # Uncomment the next line to enable the admin:
    'django.contrib.admin',
    # Uncomment the next line to enable admin documentation:
    'django.contrib.admindocs',
    'django.contrib.humanize',
    'monitoreo.lugar',
    'monitoreo.simas',
    'monitoreo.indicador01',
    'monitoreo.indicador02',
    'monitoreo.indicador05',
    'monitoreo.indicador06',
    'monitoreo.indicador07',
    'monitoreo.indicador08',
    'monitoreo.indicador09',
    'monitoreo.indicador10',
    'monitoreo.indicador11',
    'monitoreo.indicador12',
    'monitoreo.indicador13',
    'monitoreo.indicador14',
    'monitoreo.indicador15',
    'monitoreo.indicador16',
    'monitoreo.indicador17',
    'monitoreo.indicador18',
    'monitoreo.indicador19',
    'monitoreo.indicador20',
    'south',
)

NO_DATA_GRAPH_URL = '/'
