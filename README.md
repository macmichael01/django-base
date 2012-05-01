**ABOUT**

Django Base is an automated way to create a Django project directory structure. Once installed, creating a new Django project is as easy as running the following command from a terminal: mkdjango project_name.

Directory structure is as follows:

    Project/
    |-- .gitignore
    |-- conf/ (Server configurations)
    |   |-- apache.conf
    |   |-- nginx.conf
    |   |-- requirements.txt
    |
    |-- docs/
    |   |-- <Documentation Here>
    |
    |-- fabfile.py
    |-- media/
    |   |-- <Uploaded Media Here>
    |
    |-- README
    |-- Project/
    |    |-- apps/
    |    |   |-- <Django Apps Here>
    |    |
    |    |-- settings.py
    |    |-- settings_local.py
    |    |-- static/
    |    |   |-- CACHE/
    |    |   |   |-- css/
    |    |   |   |   |-- <Compiled CSS Here>
    |    |   |   |   |
    |    |   |   |-- js/
    |    |   |       |-- <Compiled JS Here> 
    |    |   |
    |    |   |-- css/
    |    |   |   |-- base.css
    |    |   |   |-- reset.css
    |    |   |
    |    |   |-- img/
    |    |   |   |-- <Static Images Here>
    |    |   |
    |    |   |-- js/
    |    |      |-- base.js
    |    |
    |    |-- wsgi.py
    |
    |-- templates/
    |   |-- base.html
    |   |-- index.html
    |
    |-- urls.py

**INSTALLATION**

    git clone https://github.com/macmichael01/django-base;
    cd django-base;
    sudo python setup.py install;

OR

    easy_install django-base

**USAGE**

    usage: Django Base [-h] [--hostname HOSTNAME] [--port PORT] [--dest DEST]
                       [--path PATH] [--database DATABASE] [--config CONFIG]
                       [--template TEMPLATE] [-w] [-v] [--version]
                       [project]

    Django-base project creator. v1.0

    positional arguments:
      project              Project name. default: example

    optional arguments:
      -h, --help           show this help message and exit
      --hostname HOSTNAME  hostname, default: localhost
      --port PORT          port, default: 80
      --dest DEST          destination folder, default: CWD
      --path PATH          project production server path.
      --database DATABASE  database module to use, choices: postgresql_psycopg2,
                           postgresql, mysql, sqlite3 or oracle, default:
                           postgresql_psycopg2
      --config CONFIG      1) Apache WSGI, 2) Apache WSGI with SSL, 3) Nginx proxy
                           & media server, with Apache WSGI, 4) Nginx proxy &
                           media server with SSL, with Apache WSGI with SSL
                           forwarding
      --template TEMPLATE  custom project template directory
      -w, --wizard         step-by-step wizard.
      -v, --verbose        display verbosity
      --version            show program's version number and exit

When using a custom template directory, the following variables can be used:

    {{ PROJECT }} - project name
    {{ SECRET }} - secret key
    {{ HOSTNAME }} - hostname
    {{ DATABASE }} - Django Database module
    {{ CONFIG }} - configuration setting [1-4]
    {{ PORT }} - port number determined by configuration setting [1-2 = 80], [3-4=8080]
    {{ PATH }} - /path/to/project/
    {{ PROJECTPATH }} - /path/to/project/project_name
    {{ VERSION }} - Django version

*NOTE*: The library makes use of argparse which is made available by default in python 2.7.
