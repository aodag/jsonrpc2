.. -*- restructuredtext -*-

.. image:: https://drone.io/bitbucket.org/aodag/jsonrpc2/status.png
   :target: https://drone.io/bitbucket.org/aodag/jsonrpc2/latest

jsonrpc2 is WSGI Framework for JSON RPC 2.0.

JSON RPC 2.0 Spec can be seen on http://www.jsonrpc.org/specification .

.. contents::

QuickStart
==========================================

install via pip::

 $ pip install jsonrpc2

write your procedures in hello.py::

 def greeting(name):
     return dict(message="Hello, %s!" % name)

run jsonrpc2 server::

 $ runjsonrpc2 hello


Integration with Paste Script
===============================================

create project with paste script template::

 $ paster create -t paster_jsonrpc2 myrpc
 $ cd myrpc

run server

 $ paster serve run.ini

access http://localhost:8080/


Internal
===============================

::

 >>> import json
 >>> from jsonrpc2 import JsonRpcApplication

sample procedure::

 >>> def greeting(name="world"):
 ...     return "Hello, %s!" % name

create rpc application::

 >>> app = JsonRpcApplication(rpcs=dict(greeting=greeting))

set up for test::

 >>> from webtest import TestApp
 >>> testapp = TestApp(app)

call procedure::

 >>> call_values = {'jsonrpc':'2.0', 'method':'greeting', 'id':'greeting'}
 >>> res = testapp.post('/', params=json.dumps(call_values), content_type="application/json")

got results::

 >>> res.json
 {u'jsonrpc': u'2.0', u'id': u'greeting', u'result': u'Hello, world!'}


lazy loading::

 >>> app.rpc.methods['sample.add'] = 'tests.sample:add'
 >>> call_values = {'jsonrpc':'2.0', 'method':'sample.add', 'id':'sample.add', 'params':[1, 2]}
 >>> res = testapp.post('/', params=json.dumps(call_values), content_type="application/json")
 >>> res.json
 {u'jsonrpc': u'2.0', u'id': u'sample.add', u'result': 3}


extra vars
==================

::

 >>> from jsonrpc2 import JsonRpc
 >>> rpc = JsonRpc()
 >>> rpc['add'] = lambda a, b: a + b
 >>> rpc({'jsonrpc': '2.0', 'method': 'add', 'id': 'rpc-1', 'params': {'a': 2}}, b=3)
 {'jsonrpc': '2.0', 'id': 'rpc-1', 'result': 5}

handle errors
=================

::

 >>> from jsonrpc2 import JsonRpc
 >>> class MyException(Exception):
 ...     pass
 >>> def my_rpc():
 ...     raise MyException()
 >>> rpc = JsonRpc({'call': my_rpc}, {MyException: -32001})
 >>> rpc({'jsonrpc': '2.0', 'method': 'call', 'id': 'rpc-1', 'params': []})
 {'jsonrpc': '2.0', 'id': 'rpc-1', 'error': {'message': '', 'code': -32001, 'data': '[]'}}

