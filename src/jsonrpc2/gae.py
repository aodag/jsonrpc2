"""
for the google appengine handler
"""
from jsonrpc2 import JsonRpc
import json

rpc = JsonRpc()

def register(namespace=None, name=None):
    def wrap(func):
        if name is None:
            name = func.__name__
        if nemspace is None:
            rpc.methods[name] = func
        else:
            rpc.methods[namespace + '.' + name] = func
        return func
    return wrap



class JsonRpcHandlerMixin(object):
    def post(self):
        try:
            body = environ['wsgi.input'].read(-1)
            data = json.loads(body)
            resdata = rpc(data) 
        except ValueError, e:
            resdata = {'jsonrpc':'2.0',
                       'id':None,
                       'error':{'code':PARSE_ERROR,
                                'message':errors[PARSE_ERROR]}}
        self.response.headers['Content-type'] = 'application/json'
        if resdata:
            self.response.out.write(json.dumps(resdata))


