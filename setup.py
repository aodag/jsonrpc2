from setuptools import setup, find_packages
import os
here = os.path.dirname(__file__)
readme = open(os.path.join(here, "README.rst")).read()
example = open(os.path.join(here, "rpc_example.txt")).read()
changelog = open(os.path.join(here, "ChangeLog")).read()
version="0.4"

tests_require = [
    "pytest",
    "pytest-cov",
    "WebTest",
]

setup(
    name="jsonrpc2",
    description="WSGI Framework for JSON RPC 2.0",
    long_description=readme + "\n" + example + "\n" + changelog,
    classifiers=[
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Topic :: Internet :: WWW/HTTP :: WSGI",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.2",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        ],
    author='Atsushi Odagiri',
    author_email='aodagx@gmail.com',
    keywords='wsgi request web http json rpc',
    license="MIT",
    url='http://hg.aodag.jp/jsonrpc2/',
    version=version,
    install_requires=[
        "six",
    ],
    include_package_data=True,
    test_suite="jsonrpc2",
    tests_require=tests_require,
    extras_require={
        "PASTE":[
            "PasteScript",
        ],
        "test":tests_require,
    },
    packages=find_packages(exclude=['tests']),
    entry_points={
        "console_scripts":[
            "runjsonrpc2=jsonrpc2.cmd:main",
        ],
        "paste.app_factory":[
            "main=jsonrpc2.paste:make_app",
        ],
        "paste.paster_create_template":[
            "paster_jsonrpc2=jsonrpc2.paste.templates:JsonRpcTemplate",
        ],
    },
)

