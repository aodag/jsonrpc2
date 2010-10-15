from setuptools import setup, find_packages
import os
here = os.path.dirname(__file__)
readme = open(os.path.join(here, "README.txt")).read()
version="0.2"

setup(
    name="jsonrpc2",
    description="WSGI Framework for JSON RPC 2.0",
    long_description=readme,
    classifiers=[
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Topic :: Internet :: WWW/HTTP :: WSGI",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
        ],
    author='Atsushi Odagiri',
    author_email='aodagx@gmail.com',
    keywords='wsgi request web http json rpc',
    license="MIT",
    url='http://bitbucket.org/aodag/microapps/overview/',
    version=version,
    install_requires=[
        "simplejson",
        "WebOb",
    ],
    package_dir={'':'src'},
    test_suite="nose.collector",
    tests_require=[
        "Nose",
        "WebTest",
        ],
    packages=find_packages("src", exclude=['tests']),
)

