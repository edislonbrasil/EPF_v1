from setuptools import setup, find_packages

setup(
    name = 'EPF_v1',
    version = '0.1.0',
    url = 'https://github.com/edislonbrasil/EPF_v1',
    description = 'Tools for Electricity Price Forecasting',
    packages = find_packages(include=['EPF_v1', 'EPF_v1.*']),
    install_requires = ['pandas>=1', 'numpy>=1'
      ]
)
