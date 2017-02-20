#coding:utf-8

from setuptools import setup, find_packages 

setup(
    name='f42',
    version="0.1.3", 
    description="Some common use functions", 
    author="Lerry",
    author_email="lvdachao@gmail.com",
    packages = ['f42'],
    zip_safe=False,
    include_package_data=True,
    install_requires = [
    ],
    url = "https://bitbucket.org/vcwatch/f42",
)

