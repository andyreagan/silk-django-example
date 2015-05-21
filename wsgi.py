#! /usr/bin/env python
import os, sys
sys.path.append('/users/c/m/cmplxsys/www-root/pythonstuff/testsite')
os.environ['DJANGO_SETTINGS_MODULE'] = 'testsite.settings'

import django.core.handlers.wsgi

_application = django.core.handlers.wsgi.WSGIHandler()

def application(environ, start_response):
    # environ['PATH_INFO'] = environ['SCRIPT_NAME'] + environ['PATH_INFO']
    result = _application(environ, start_response)
    yield '%s'  % result
request_handler = application

