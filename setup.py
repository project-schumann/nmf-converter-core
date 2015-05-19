from setuptools import setup

setup(
  name='vmf-converter',
  packages=['vmf_converter'],
  version='0.0.1',
  description='VMF Converter for Music21',
  long_description = open('README.rst', 'r').read(),
  author = 'Patrick Ayoup',
  author_email = 'patrick.ayoup@gmail.com',
  license = 'MIT',
  url='https://github.com/project-schumann/vmf-converter/',
  download_url='https://github.com/project-schumann/vmf-converter/tarball/0.0.1',
  keywords = ['music', 'vector', 'notation'],
  classifiers = [
    'Development Status :: 5 - Production/Stable',
    'Environment :: Console',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: MIT License',
    'Natural Language :: English',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Programming Language :: Python :: 3.4',
    'Topic :: Utilities'
  ]
)