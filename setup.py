from distutils.core import setup
setup(
  name = 'cmdtools',
  packages = ['cmdtools'],
  version = '0.0.1',
  description = 'Tools for processing and uploading cmd datasets',
  author = 'James Bryant',
  author_email = 'james.bryant@ons.gov.uk',
  url = 'https://github.com/GSS-Cogs/cmd-tools',
  download_url = 'https://github.com/GSS-Cogs/cmdtools/archive/0.0.1.tar.gz',
  keywords = ['databaker', 'pandas', 'cmd', ''],
  classifiers = [],
  entry_points={
        'console_scripts': [
            'cmdtools.commandline:cmdload'
        ]
  }
)