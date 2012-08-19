import sys
from setuptools import setup
from setuptools.command.test import test as TestCommand

long_description="""
What is Tox?
==========================

Tox as is a generic virtualenv management and test command line tool you can
use for:

* checking your package installs correctly with different
  Python versions and interpreters

* running your tests in each of the
  environments, configuring your test tool of choice

* acting as a frontend to Continuous Integration
  servers, greatly reducing boilerplate and merging
  CI and shell-based testing.

For more information, docs and many examples please checkout the `home page`_:

    http://tox.testrun.org/

.. _`home page`: http://tox.testrun.org/
"""

class Tox(TestCommand):
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True
    def run_tests(self):
        #import here, cause outside the eggs aren't loaded
        import tox
        tox.cmdline(self.test_args)

def main():
    version = sys.version_info[:2]
    install_requires = ['virtualenv>=1.7', 'py>=1.4.9', ]
    if version < (2,7) or (3,0) <= version <= (3,1):
        install_requires += ['argparse']
    setup(
        name='tox',
        description='virtualenv-based automation of test activities',
        long_description=long_description,
        url='http://tox.testrun.org/',
        version='1.4.3.dev0',
        license='GPLv2 or later',
        platforms=['unix', 'linux', 'osx', 'cygwin', 'win32'],
        author='holger krekel',
        author_email='holger@merlinux.eu',
        packages=['tox', ],
        entry_points={'console_scripts': 'tox=tox:cmdline'},
        # we use a public tox version to test, see tox.ini's testenv
        # "deps" definition for the required dependencies
        tests_require=['tox'],
        cmdclass={"test": Tox},
        install_requires=install_requires,
        zip_safe=True,
        classifiers=[
            'Development Status :: 5 - Production/Stable',
            'Intended Audience :: Developers',
            'License :: OSI Approved :: GNU General Public License (GPL)',
             'Operating System :: POSIX',
             'Operating System :: Microsoft :: Windows',
             'Operating System :: MacOS :: MacOS X',
             'Topic :: Software Development :: Testing',
             'Topic :: Software Development :: Libraries',
             'Topic :: Utilities',
             'Programming Language :: Python',
             'Programming Language :: Python :: 3'],
    )

if __name__ == '__main__':
    main()
