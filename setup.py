from setuptools import setup, find_packages

setup(
    name = 'epfv1',
    version = '0.1.0',
    url = 'https://github.com/edislonbrasil/epfv1',
    description = 'Tools for Electricity Price Forecasting',
    packages = find_packages(include=['epfv1', 'epfv1.*']),
    install_requires = ['pandas>=1', 'numpy>=1'
      ]
)
