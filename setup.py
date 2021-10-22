from setuptools import setup

with open('README.md', 'r') as f:
    long_description = f.read()

setup(
    name='r_logger',
    version="0.1.0",
    packages=['r_logger'],
    author="Ramin Zarebidoky",
    author_email="ramin.zarebidoky@gmail.com",
    description="a customized way to use log",
    url="https://github.com/RaminZarebidoky/r_config",
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=[]
)
