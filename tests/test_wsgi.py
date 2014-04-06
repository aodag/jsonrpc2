#
from webtest import TestApp
from testfixtures import compare
#from nose import with_setup
#from nose.tools import *
from jsonrpc2 import JsonRpcApplication
from functools import wraps
import sys
try:
    import json
except ImportError:
    import simplejson as json
    sys.moduels['json'] = json


def _make_app():
    app = JsonRpcApplication()
    app.rpc['hello'] = lambda x : {"message":"hello %s" % x}
    app = TestApp(app)
    return app

def test_failure():
    app = _make_app()
    params = json.dumps({'jsonrpc':'2.0', 
        'method':'hello', 
        'params':"a", 
        'id':'hello'})
    res = app.post('/', params=params,
            extra_environ={
                "CONTENT_TYPE":'application/json',
                })

    compare(res.json, 
            {"jsonrpc": "2.0", 
             "id": "hello", 
             "error": {"message": "Invalid Params", "code": -32602}})

