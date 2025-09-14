## for hosting change the base directory of the server dynamically on settings.py

import os
BASE_DIR = Path(__file__).resolve().parent.parent

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
] 


##change the wsgi configuration file to 

import os
import sys

# Full path to your Django project root (where manage.py is)
path = '/home/anjan095/TodoDjango'
if path not in sys.path:
    sys.path.append(path)

# Your Django settings module (project_name.settings)
os.environ['DJANGO_SETTINGS_MODULE'] = 'todo.settings'

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
