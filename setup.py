import os
from setuptools import setup, find_packages

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

from gtm import __version__

setup(
    name = "django-google-tag-manager",
    version = __version__,
    author = "Tomas Neme",
    author_email = "lacrymology@gmail.com",
    description = ("Easily include your Google Tag Manager tag in your "
                   "django site"),
    license = "MIT",
    keywords = "django generic-views",
    url = "https://github.com/Lacrymology/django-google-tag-manager",
    packages=find_packages(),
    include_package_data=True,
    long_description=read('README.md'),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: MIT License",
    ],
)
