jsonrpc2 is WSGI Framework for JSON RPC 2.0.
JSON RPC 2.0 Spec can be seen on http://groups.google.com/group/json-rpc/web/json-rpc-2-0

>>> import simplejson as json
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
{'jsonrpc': '2.0', 'id': 'greeting', 'result': 'Hello, world!'}
