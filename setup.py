from setuptools import setup, find_packages
import os
here = os.path.dirname(__file__)
readme = open(os.path.join(here, "README")).read()
example = open(os.path.join(here, "rpc_example.txt")).read()
changelog = open(os.path.join(here, "ChangeLog")).read()
version="0.2.3"

setup(
    name="jsonrpc2",
    description="WSGI Framework for JSON RPC 2.0",
    long_description=readme + "\n" + example + "\n" + changelog,
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
    url='http://hg.aodag.jp/jsonrpc2/',
    version=version,
    install_requires=[
    ],
    package_dir={'':'src'},
    include_package_data=True,
    test_suite="nose.collector",
    tests_require=[
        "Nose",
        "WebTest",
        "simplejson",
        ],
    extras_require={
        "PASTE":[
            "PasteScript",
        ],
    },
    setup_requires=[
        "Nose",
        "hg.setuptools",
        ],
    packages=find_packages("src", exclude=['tests']),
    entry_points={
        "paste.app_factory":[
            "main=jsonrpc2.paste:make_app",
        ],
        "paste.paster_create_template":[
            "paster_jsonrpc2=jsonrpc2.paste.templates:JsonRpcTemplate",
        ],
    },
)

