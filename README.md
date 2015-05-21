A bare-bones example of a python app, specifically Django, running in a subfolder on UVMs silk server

Instructions:

You're going to need pip.
From your top level directory (above `www-root`), get the installation file:

    wget https://bootstrap.pypa.io/get-pip.py
    
and then run it

    python get-pip.py --user
    
Since the python is older, it will only support the older Django, get that:

    .local/bin/pip install --user django==1.6.5
    
Now go ahead and make a folder inside `www-root`:

    mkdir www-root/pythonstuff
    cd www-root/pythonstuff
    
and start your django project.
From here, you can follow along, or just clone this repository into that folder.
To make you own site from scratch:

    ../../.local/bin/django-admin.py startproject testsite

sync the database

    python manage.py syncdb
    
and make sure to get the .htaccess out of this repo. Done!
Set up `urls.py` accordingly.

Here is a look at what I've got installed:

    ../../.local/bin/pip freeze >> requirements.txt
