#!/usr/bin/env python
import os
import sys
import unittest
from setuptools import Command
from distutils.core import setup


def get_files(root):
    for dirname, dirnames, filenames in os.walk(root):
        for filename in filenames:
            yield os.path.join(dirname, filename)


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


class BotTest(Command):
    """
    Run the tests for Hubot Webhook
    """
    description = "Run tests for portal"

    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        if self.distribution.tests_require:
            self.distribution.fetch_build_eggs(self.distribution.tests_require)

        from tests import suite
        test_result = unittest.TextTestRunner(verbosity=2).run(suite())

        if test_result.wasSuccessful():
            sys.exit(0)
        sys.exit(-1)


MODULE = "bot"
PREFIX = "my"


setup(
    name='%s-%s' % (PREFIX, MODULE),
    packages=['bot'],
    url='https://www.github.com/rajatguptarg/hubot-webhook',
    license='MIT',
    author='Rajat Gupta',
    author_email='rajat.gupta712@gmail.com',
    description='Webhook Service for Hubot',
    zip_safe=False,
    classifiers=[
        'Development Status :: 1 - Planning',
        'Environment :: Plugins',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Flask',
        'Topic :: Office/Business',
    ],
    test_suite='tests.suite',
    tests_require=[],
    cmdclass={
        'test': BotTest,
    },
)
