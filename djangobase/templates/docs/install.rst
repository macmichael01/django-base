==================
Installation Guide
==================

Pre-Requisites
--------------

* `setuptools <http://pypi.python.org/pypi/setuptools>`_
* `virtualenv <http://pypi.python.org/pypi/virtualenv>`_
* `pip <http://pypi.python.org/pypi/pip>`_

Debian-based install::

  sudo apt-get install python-setuptools python-pip python-virtualenv

Checkout the project
--------------------

    git clone git@{{ HOSTNAME }}:{{ PROJECT }}.git

Configure the virtual environment
---------------------------------

::

    cd {{ LOCALPATH }}
    virtualenv env
    source env/bin/activate
    # Install project dependencies
    pip install -r conf/requirements.pip

Configure the database
----------------------

Database parameters::

    DATABASE_NAME = '{{ PROJECT }}'
    DATABASE_USER = '{{ PROJECT }}'

{% if DATABASE == 'postgresql_psycopg2' %}**Using PostgreSQL**

Login under the given UNIX user (normally postgres) with permission to use
the following PostgreSQL terminal commands::


    createuser -A -D -P {{ PROJECT }}
    createdb -O {{ PROJECT }} {{ PROJECT }}
    # If using PostGIS use the following to create your database
    createdb -O {{ PROJECT }} {{ PROJECT }} -T template_postgis
{% endif %}{% if DATABASE == 'mysql' %}**Using MySQL**

From the Terminal login to the MySQL shell and run the following commands::


    mysql -uroot -p
    mysql> CREATE DATABASE {{ PROJECT }} CHARACTER SET utf8;
    mysql> GRANT ALL ON {{ PROJECT }}.* TO {{ PROJECT }}@localhost IDENTIFIED BY 'some_passwd';
    mysql> GRANT ALL ON {{ PROJECT }}.* TO {{ PROJECT }}@localhost IDENTIFIED BY 'some_passwd';
{% endif %}{% if DATABASE == 'sqlite3' %}**Using SQLite**::{% endif %}{% if DATABASE != 'sqlite3' %}
For quick database configuration use the SQLite database setting 
in settings_local.py::
{% endif %}

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': '{{ LOCALPATH }}/db/{{ PROJECT }}.db'
        }
    }

    cd {{ LOCALPATH }}/{{ PROJECT }}
    ./manage.py syncdb

Production Configuration and Deployment
---------------------------------------

Projects, by default, are setup to use fabric::

    cd {{ LOCALPATH }}
    fab deploy

# Further configuration & deployment here...

Building Documentation
----------------------

Documentation is available in ``docs`` and can be built into a number of 
formats using `Sphinx <http://pypi.python.org/pypi/Sphinx>`_. To get started::

    pip install Sphinx
    cd {{ LOCALPATH }}/docs
    make html

This creates the documentation in HTML format at ``docs/_build/html``.
