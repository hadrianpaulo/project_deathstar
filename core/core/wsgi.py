"""
WSGI config for core project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/howto/deployment/wsgi/
"""

import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings.prod")

activate_this = os.path.join("/home/fassster/virtualenvs/prod", 'bin', 'activate_this.py')

with open(activate_this) as file_:
    exec(file_.read(), dict(__file__=activate_this))

application = get_wsgi_application()
