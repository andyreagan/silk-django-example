A bare-bones example of a python app, specifically Django, running in a subfolder on UVMs silk server

.local/bin/pip install --user django==1.6.5

../.local/bin/django-admin.py startproject testsite

python manage.py syncdb
../../.local/bin/pip freeze >> requirements.txt
