import os
from setuptools import setup

with open(os.path.join(os.path.dirname(__file__), 'README.markdown')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-semantic-ui',
    version='0.1',
    packages=['semantic_ui'],
    include_package_data=True,
    description='An Django application for semantic ui templates helpers',
    long_description=README,
    url='https://github.com/gpichot/django-semantic-ui',
    author='Gabriel Pichot',
    author_email='me@gabrielpichot.com',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Utilities',
    ],
)
