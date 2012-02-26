**ABOUT**

Django Base is an automated way to create a Django project directory structure. Once installed, creating a new django project is as easy as running the following command from a terminal: mkdjango project_name.

Directory structure is as follows:

    project_name/
        .gitignore
        conf/ (Server configurations)
            apache.conf
            django.wsgi
            nginx.conf
            requirments.txt
        fabfile.py (Deployment script)
        media/ (Uploaded media)
        README
        trunk/
            apps/ (project apps here)
            settings.py
            settings_local.py
            static/
                CACHE/ (Compiled CSS and JS)
                css/
                    base.css
                    reset.css
                img/
                js/
                    base.js
            templates/
                base.html
                index.html
            urls.py


**INSTALL**

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
      --database DATABASE   database module to use, choices: postgresql_psycopg2,
                            postgresql, mysql, sqlite3 or oracle, default:
                            postgresql_psycopg2

*NOTE*: The library makes use of argparse which was made available in python 2.7. 
