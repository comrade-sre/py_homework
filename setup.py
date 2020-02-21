from setuptools import setup, find_packages
from os.path import join, dirname

setup(
    name='tagcounter',
    version='1.0',
    test_suite='tests',
    packages=find_packages(),
    long_description=open(join(dirname(__file__), 'README.md')).read(),
    entry_points={
        'console_scripts':
            ['tagcounter = tagcounter.tagcounter:main']
        }
)