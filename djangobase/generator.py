import os, sys
import mimetypes
import random
import re
import shutil

from jinja2 import Template

__author__ = "Chris McMichael"
__version__ = "V0.96"


SOURCE = os.path.abspath(os.path.dirname(__file__))
DESTINATION = os.getcwd()


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

    def validate_projectname(self):
        if not re.search(r'^[_a-zA-Z]\w*$', self.project):
            if not re.search(r'^[_a-zA-Z]', self.project):
                message = 'Project name must begin with [a-z, A-Z, _]'
            else:
                message = 'Use characters [a-z, A-Z, 0-9, _]'
            values = dict(self.colorize, name=self.project, message=message)
            msg = "\n\n\t%(red)s%(name)s is an invalid project name. %(message)s.%(reset)s"
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
        elif self.validate_projectname():
            self.generate_secret()
            self.generate_projectpath()

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

        if self.verbose:
            print "\n%(cyan)sDone!%(reset)s" % self.colorize
