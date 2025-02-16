# coding: utf-8

import sys
from setuptools import setup, find_packages

NAME = "swagger_server"
VERSION = "1.0.0"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = ["connexion"]

setup(
    name=NAME,
    version=VERSION,
    description="Pollination Web Server",
    author_email="",
    url="",
    keywords=["Swagger", "Pollination Web Server"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['swagger/swagger.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['swagger_server=swagger_server.__main__:main']},
    long_description="""\
    All values in this API are required and not nullable unless specifically stated.  Org user privileges are:&lt;br&gt;  0 :&#x3D; removed&lt;br&gt;  1 :&#x3D; invited&lt;br&gt;  2 :&#x3D; member&lt;br&gt;  3 :&#x3D; admin&lt;br&gt;  4 :&#x3D; owner 
    """
)
