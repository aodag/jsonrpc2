from paver.easy import *
from paver.virtual import bootstrap

options.virtualenv = {
    "distribute":True,
    "packages_to_install":[
        "nose",
        "simplejson",
        "WebTest",
        "docutils",
    ],
    "no_site_packages":True,
}
