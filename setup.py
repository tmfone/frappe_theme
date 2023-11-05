from setuptools import setup, find_packages
import os

version = '0.0.1'

setup(
    name='frappe_theme',
    version=version,
    description='Theme for Frappe sites',
    author='tmf.one',
    author_email='lab@tmf.one',
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    install_requires=("frappe",),
)
