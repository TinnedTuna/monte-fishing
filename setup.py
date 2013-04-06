from setuptools import setup

requires = [
        'straight.plugin',
        'nose',
        ]

setup(name='monte_fishing',
      version='0.0',
      packages=['monte_fishing'],
      test_suite='monte_fishing.tests',
      install_requires=requires
     )
