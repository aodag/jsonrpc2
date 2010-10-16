jsonrpc2 is WSGI Framework for JSON RPC 2.0.
JSON RPC 2.0 Spec can be seen on http://groups.google.com/group/json-rpc/web/json-rpc-1-2-proposal.

>>> from jsonrpc2 import JsonRpcApplication
>>> def greeting(name="world"):
...     return "Hello, %s!" % name
>>> app = JsonRpcApplication(rpcs=dict(greeting=greeting))
>>> from webtest import TestApp
>>> testapp = TestApp(app)
>>> call_values = {'jsonrpc':'2.0', 'method':'greeting', 'id':'greeting'}
>>> import simplejson as json
>>> res = testapp.post('/', params=json.dumps(call_values), content_type="application/json")
>>> res.json
{'jsonrpc': '2.0', 'id': 'greeting', 'result': 'Hello, world!'}
