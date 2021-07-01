"""The setup script."""

from setuptools import find_packages, setup

test_requirements = ['pytest', ]

setup(
   name="ci_demo",            # name of your package
   version="0.0.1",
   packages=find_packages(include=['datascience_schedule']),     
   test_suite='tests',
   tests_require=test_requirements,
)