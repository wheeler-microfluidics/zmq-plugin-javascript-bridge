import sys

from paver.easy import task, needs, path, sh, cmdopts, options
from paver.setuputils import setup, install_distutils_tasks
from distutils.extension import Extension
from distutils.dep_util import newer

sys.path.insert(0, path('.').abspath())
import version

setup(name='zmq-plugin-javascript-bridge',
      version=version.getVersion(),
      description='JavaScript bridge for a ZeroMQ-based spoke-hub plugin framework.',
      keywords='',
      author='Ryan Fobel',
      author_email='ryan@fobel.net',
      url='https://github.com/wheeler-microfluidics/zmq-plugin-javascript-bridge',
      license='GPL',
      packages=['zmq_plugin_javascript_bridge', ],
      install_requires=['zmq-plugin'],
      # Install data listed in `MANIFEST.in`
      include_package_data=True)


@task
@needs('generate_setup', 'minilib', 'setuptools.command.sdist')
def sdist():
    """Overrides sdist to make sure that our setup.py is generated."""
    pass
