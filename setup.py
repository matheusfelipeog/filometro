# -*- coding: utf-8 -*-

import os
import sys
from shutil import rmtree
from setuptools import setup, find_packages, Command

from filometro import __version__
from filometro import __author__


here = os.path.abspath(os.path.dirname(__file__))


class PublishCommand(Command):
    """Support setup.py publish."""

    description = 'Build and publish package in Pypi.'
    user_options = []

    @staticmethod
    def print_status(msg):
        """Prints message in bold and yellow."""
        print('\033[1;33m{m}\033[0m'.format(m=msg))

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        try:
            self.print_status('Removing previous builds…')

            rmtree(os.path.join(here, 'dist'))
            rmtree(os.path.join(here, 'build'))

        except OSError:
            pass
        
        self.print_status('Build Source and Wheel distribution…')
        os.system('{python} setup.py sdist bdist_wheel'.format(python=sys.executable))

        self.print_status('Uploading the package to PyPi via Twine…')
        os.system('twine upload --config-file .pypirc --repository pypi dist/*')

        sys.exit()


with open(os.path.join(here, 'README.md'), mode='r', encoding='utf-8') as f:
    long_description = '\n' + f.read()


setup(
    name='filometro',
    version=__version__,
    description='Um wrapper Python do site "De Olho na Fila": obtenha os dados dos postos de vacinação da covid-19 em São Paulo',
    long_description=long_description,
    long_description_content_type='text/markdown',
    license='MIT License',
    author=__author__,
    author_email='matheusfelipeog@protonmail.com',
    url='https://github.com/matheusfelipeog/filometro',
    packages=find_packages(
        exclude=('tests',)
    ),
    install_requires=[
        'requests>=2.27.1',
        'pandas>=1.4.1'
    ],
    zip_safe=False,
    python_requires='>=3.7',
    project_urls={
        "Bug Tracker": "https://github.com/matheusfelipeog/filometro/issues",
        "Documentation": "https://github.com/matheusfelipeog/filometro/tree/master#documentação",
        "Source Code": "https://github.com/matheusfelipeog/filometro",
    },
    keywords=[
        'filometro', 'de-olho-na-fila', 'data', 'sao-paulo',
        'covid-19', 'vacina', 'vacinasampa', 'python', 'wrapper'
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: Portuguese (Brazilian)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: Implementation :: CPython',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
    # setup.py publish support
    cmdclass={
        'publish': PublishCommand
    }
)