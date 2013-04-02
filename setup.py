import os
import sys

from distutils.core import setup

BASE_DIR = os.path.dirname(__file__) or os.getcwd()
MODULES = [x.replace('.py', '') for x in filter(lambda x: x != 'setup.py' and x.endswith('py'), os.listdir(BASE_DIR))]

PLUGINS_DIR = 'KalturaPlugins'
plugins_init_file = os.path.join(BASE_DIR, PLUGINS_DIR, '__init__.py')
if not os.path.exists(plugins_init_file):
    open(plugins_init_file, 'ab').close()

setup(
    name='kaltura',
    version='3.1.5',
    py_modules=MODULES,
    packages = [PLUGINS_DIR],
)
