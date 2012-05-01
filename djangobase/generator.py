import os, sys
import mimetypes
import random
import re
import shutil

from jinja2 import Template

__author__ = "Chris McMichael"
__version__ = "v1.0"


SOURCE = os.path.abspath(os.path.dirname(__file__))
DESTINATION = os.getcwd()
CONFIG = """
    1) Apache WSGI,
    2) Apache WSGI with SSL,
    3) Nginx proxy & media server, with Apache WSGI,
    4) Nginx proxy & media server with SSL, with Apache WSGI with SSL forwarding
"""

class GenerateProject(object):

    def __init__(self, project, hostname='localhost', port=80,
        dest=DESTINATION, path='/usr/local/projects',
        database='postgresql_psycopg2', template=None, config=3, wizard=False,
        verbose=False, version=__version__, *args, **kwargs):

        self.project = project
        self.hostname = hostname
        self.dest = dest
        self.port = port
        self.database = database
        self.config = config
        self.wizard = wizard
        self.verbose = verbose
        self.version = version
        self.template = template
        self.projectpath = ''
        self.path = "/usr/local/projects"
        self.colorize = {
            'cyan': '\033[36m',
            'red': '\033[31m%',
            'reset': '\033[0m',
        }

    def run_wizard(self):

        # Project Name
        text = "Project name: "
        if self.project:
            text = "Project name [%s]: " % self.project

        values = dict(self.colorize, question=text)
        while True:
            question = "%(cyan)s%(question)s%(reset)s" % values
            value = raw_input(question)

            if value:
                self.project = value

            if self.validate_projectname():
                break

        # Server config.
        text = ""
        while True:
            if not text:
                text = "Server configuration: \nChoices:%s\nChoice [3]: " % CONFIG
            else:
                text = "Choice [3]: "
            values = dict(self.colorize, question=text)
            question = "%(cyan)s%(question)s%(reset)s" % values
            self.config = raw_input(question)

            if not self.config:
                self.config = 3
                break

            try:
                self.config = int(self.config)
                if self.config in [1, 2, 3, 4]:
                    break
                err = "\n\t%(red)sInvalid choice%(reset)s\n" % values
                print err
            except ValueError:
                err = "\n\t%(red)sInvalid choice%(reset)s\n" % values
                print err

        # Host
        text = "Hostname [localhost]: "
        values = dict(self.colorize, question=text)
        question = "%(cyan)s%(question)s%(reset)s" % values
        self.hostname = raw_input(question)
        if not self.hostname:
            self.hostname = 'localhost'
        
        # Port
        default_port = 80
        if self.config in [3, 4]:
            default_port = 8080
        text = "Port [%s]: " % default_port
        values = dict(self.colorize, question=text)
        question = "%(cyan)s%(question)s%(reset)s" % values
        while True:
            self.port = raw_input(question)
            if not self.port:
                self.port = default_port
                break
            try:
                self.port = int(self.port)
                break
            except ValueError:
                err = "\n\t%(red)sInvalid port%(reset)s\n" % values
                print err

        # Django Version
        text = "Django version [1.4]: "
        values = dict(self.colorize, question=text)
        question = "%(cyan)s%(question)s%(reset)s" % values
        while True:
            self.version = raw_input(question)
            if not self.version:
                self.version = 1.4
                break
            try:
                self.version = float(self.version)
                break
            except ValueError:
                err = "\n\t%(red)sInvalid Django version%(reset)s\n" % values
                print err

        # Production Server Path.
        text = "Project production server path [/usr/local/projects]: "
        values = dict(self.colorize, question=text)
        question = "%(cyan)s%(question)s%(reset)s" % values
        self.path = raw_input(question)
        if not self.path:
            self.path = "/usr/local/projects"
 
        # Custom project template directory
        text = "Custom project template directory: "
        values = dict(self.colorize, question=text)
        question = "%(cyan)s%(question)s%(reset)s" % values
        while True:
            self.template = raw_input(question)
            if not self.template:
                break
            if os.path.isdir(self.template):
                break
            err = "\n\t%(red)sInvalid template directory%(reset)s\n" % values
            print err 

        # Project output directory
        text = "Output project [%s]: " % DESTINATION
        values = dict(self.colorize, question=text)
        question = "%(cyan)s%(question)s%(reset)s" % values
        self.dest = raw_input(question)
        if not self.dest:
            self.dest = DESTINATION

    def validate_projectname(self):
        if not re.search(r'^[_a-zA-Z]\w*$', self.project):
            if not re.search(r'^[_a-zA-Z]', self.project):
                message = 'Project name must begin with [a-z, A-Z, _]'
            else:
                message = 'Use characters [a-z, A-Z, 0-9, _]'
            values = dict(self.colorize, name=self.project, message=message)
            msg = "\n\t%(red)s%(name)s is an invalid project name. %(message)s.%(reset)s\n"
            print  msg % values
            return False
        return True

    def generate_secret(self):
        chars = 'abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)'
        self.secret = ''.join([random.choice(chars) for i in range(50)])

    def generate_projectpath(self):
        self.projectpath = os.path.join(self.path, self.project)

    def create(self):
        if self.wizard:
            self.run_wizard()
        elif not self.validate_projectname():
            err = "\t%(red)sInvalid Project Name%(reset)s" % values
            print err
        elif self.validate_projectname():
            self.generate_projectpath()
        self.generate_secret()

        if self.template and os.path.isdir(self.template):
            source_path = os.path.abspath(self.template)
        else:
            source_path = os.path.join(SOURCE, "templates")
        dest_path = os.path.join(self.dest, self.project)

        if self.verbose:
            msg = "%(cyan)sGenerating Project...%(reset)s\n" % self.colorize
            print msg
        
        render_dict = {
            "PROJECT": self.project,
            "SECRET": self.secret,
            "HOSTNAME": self.hostname,
            "PORT": self.port,
            "DATABASE": self.database,
            'CONFIG': self.config,
            "PATH": self.path,
            "PROJECTPATH": self.projectpath,
            "VERSION": self.version,
            "APACHENAME": 'apache2', # TODO: apache2 vs httpd.
        }
        
        for root, dirs, files in os.walk(source_path):
            folder = root.replace(source_path, '')
            
            # Used only with the default project template configuration.
            # If the current directory selected is trunk rename it
            # to the project name.
            if '/trunk' in folder and self.project != 'trunk' \
            and not self.template:
                folder = folder.replace('trunk', self.project)

            dest = "%s%s" % (dest_path, folder)

            if self.verbose:
                values = dict(self.colorize, dest=dest)
                print "%(cyan)sCopying...%(reset)s %(dest)s" % values

            if not os.path.isdir(dest):
                os.mkdir(dest)

            for f in files:
                if ".pyc" in f:
                    continue

                # Used only with the default project template configuration.
                # When config setting 1 or 2 is selected ignore
                # the nginx.conf since it's not needed.
                if self.config in [1, 2] and not self.template \
                and "nginx.conf" in f:
                    continue

                old_location = os.path.join(root, f)

                # Used only with the default project template configuration.
                # to avoid installation errors, these django template
                # files had to be renamed a different extension.
                if f in ["manage.pyt", "settings.pyt"] and not self.template:
                    f = f.replace('.pyt', '.py')

                new_location = os.path.join(dest, f)

                try:
                    shutil.copy(old_location, new_location)
                except IOError:
                    pass

                if self.verbose:
                    values = dict(self.colorize, loc=new_location)
                    msg = "%(cyan)sCopying...%(reset)s %(loc)s" % values
                    print msg

                # A feature default and custom template configurations.
                # Since the templates folder might contain template code
                # don't allow files within the folder to be rendered.
                if 'templates' in new_location:
                    continue

                # Is the current file safe for template rendering?
                file_type = mimetypes.guess_type(f)[0]
                if file_type and 'text' in file_type:
                    file_in = open(new_location)
                    template = Template(file_in.read())
                    rendered_template = template.render(render_dict)
                    file_in.close()
                    file_out = open(new_location, "w")
                    file_out.write(rendered_template)

        if self.verbose or self.wizard:
            print "\n%(cyan)sDone!%(reset)s" % self.colorize
