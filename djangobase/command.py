import argparse
import os, sys
import random
import re
import shutil

from jinja2 import Template

SOURCE = os.path.abspath(os.path.dirname(__file__))
DESTINATION = os.getcwd()
FILES = ['apache.conf', 'wsgi.py', 'nginx.conf', 'settings.py', 'manage.py']


class GenerateProject(object):
    """
    usage: command.py [-h] [-H HOSTNAME] [-P PORT] [-D DEST] [--database DATABASE]
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
    """
    usage = "Django-base project creator."
    parser = argparse.ArgumentParser(description=usage)

    parser.add_argument(dest="project", type=str,
        help="project name used as project directory name.")

    parser.add_argument("-H", "--hostname", dest="hostname",
        default="localhost", type=str, help="hostname, default: localhost")

    parser.add_argument("-P", "--port", dest="port", type=int, default=8080,
       help="port number, default: 8080")

    parser.add_argument("-V", "--version", dest="version", type=float,
        default=1.4, help="Django Version 1.3 or 1.4")

    parser.add_argument("-v", "--verbose", dest="verbose", type=bool,
        default=False, help="Display verbosity")

    parser.add_argument("-D", "--dest", dest="dest", type=str,
        default=DESTINATION,
        help="destination folder, default: current working directory")

    parser.add_argument("-S", "--serverpath", dest="server_path",
        type=str, default="/usr/local/projects/",
        help="Path to the project location on the server.")

    parser.add_argument("--database", dest="database",
        type=str, default="postgresql_psycopg2",
        help="database module to use, choices: postgresql_psycopg2, "
             "postgresql, mysql, sqlite3 or oracle, "
             "default: postgresql_psycopg2")

    args_dict = parser.parse_args()

    def create(self):
        if not re.search(r'^[_a-zA-Z]\w*$', self.args_dict.project):
            if not re.search(r'^[_a-zA-Z]', self.args_dict.project):
                message = ('mmake sure the project name begins '
                           'with a letter or underscore')
            else:
                message = 'use only numbers, letters and underscores'
            print ("\n\n\t\033[31m%s is not a valid project name. "
                  "Please %s.\033[0m\n" % (
                self.args_dict.project, message))
            break

        chars = 'abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)'
        secret = ''.join([random.choice(chars) for i in range(50)])
        server_path = os.path.join(self.args_dict.server_path,
                                   self.args_dict.project)

        verbose = self.args_dict.verbose

        render_dict = {
            "PROJECT": self.args_dict.project,
            "SECRET": secret,
            "HOSTNAME": self.args_dict.hostname,
            "PORT": self.args_dict.port,
            "DATABASE": self.args_dict.database,
            "SERVER_PATH": server_path,
            "SERVERNAME": "apache", # TODO ubuntu vs centos
        }

        source_path = os.path.join(SOURCE, "project_template")
        dest_path = os.path.join(self.args_dict.dest, self.args_dict.project)

        if verbose:
            print "\033[36mGenerating Project...\033[0m\n"

        for root, dirs, files in os.walk(source_path):
            folder = root.replace(source_path, '')
            if '/trunk' in folder and self.args_dict.project != 'trunk':
                folder = folder.replace('trunk', self.args_dict.project)
            
            dest = "%s%s" % (dest_path, folder)

            if verbose:
                print "\033[36mCopying...", dest, "\033[0m"

            if not os.path.isdir(dest):
                os.mkdir(dest)
            
            for f in files:
                if ".pyc" in f:
                    continue

                old_location = os.path.join(root, f)
                new_location = os.path.join(dest, f)
                try:
                    shutil.copy(old_location, new_location)
                except IOError:
                    pass

                if verbose:
                    print "\033[36mCopying...", new_location, "\033[0m"

                if f in FILES:
                    file_in = open(new_location)
                    rendered_line = ""

                    for line in file_in:
                        template = Template(line)
                        rendered_line += "%s\n" % template.render(render_dict)

                    file_in.close()

                    file_out = open(new_location, "w")
                    file_out.write(rendered_line)

        if verbose:
            print "\n"
