# config for sphinx
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), os.pardir))
master_doc = 'index'
source_encoding = 'utf-8'
project = u'jsonrpc'
copyright = u'2010, Atsushi Odagiri'
language = "ja"
extensions = ['sphinx.ext.autodoc', 'sphinx.ext.doctest']
html_use_modindex = True

