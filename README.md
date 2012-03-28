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

    usage: mkdjango [-h] [-H HOSTNAME] [-P PORT] [-D DEST] [--database DATABASE]
                    project
    
    Django-base project creator.
    
    positional arguments:
      project               project name used as project directory name.
    
    optional arguments:
      -h, --help            show this help message and exit
      -H HOSTNAME, --hostname HOSTNAME
                            hostname, default: localhost
      -P PORT, --port PORT  port number, default: 8080
      -D DEST, --dest DEST  destination folder, default: current working directory
      -S SERVER_PATH, --serverpath SERVER_PATH
	                        Path to the project location on the server.

      --database DATABASE   database module to use, choices: postgresql_psycopg2,
                            postgresql, mysql, sqlite3 or oracle, default:
                            postgresql_psycopg2

*NOTE*: The library makes use of argparse which was made available in python 2.7. 
