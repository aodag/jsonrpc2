from setuptools import setup, find_packages
version="0.1"

setup(
    name="jsonrpc2",
    description="WSGI Framework for JSON RPC 2.0",
    long_description="""\
jsonrpc2 is WSGI Framework for JSON RPC 2.0.
JSON RPC 2.0 Spec can be seen on http://groups.google.com/group/json-rpc/web/json-rpc-1-2-proposal.


""",
    classifiers=[
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Topic :: Internet :: WWW/HTTP :: WSGI",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
        ],
    author='Atsushi Odagiri',
    author_email='aodagx@gmail.com',
    keywords='wsgi request web http',
    url='http://bitbucket.org/aodag/microapps/overview/',
    version=version,
    install_requires=[
        "simplejson",
        "WebOb",
    ],
    package_dir={'':'src'},
    packages=find_packages("src", exclude=['tests']),
)

