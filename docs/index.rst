================
JSON RPC2
================
jsonrpc2は、JSON RPCによる呼び出しを可能にするWSGIアプリケーションです。
`JSON RPC Spec2 Draft <http://groups.google.com/group/json-rpc/web/json-rpc-1-2-proposal>`_
に準拠させるようにしています。
JSONパーサーは、json, django.utils.simplejson, simplejsonを順に検索して最初に見つかったものを利用します。

インストール方法
==================================================================

easy_install::
 easy_install -f jsonrpc2


基本的な使い方
==================================================================

>>> from webtest import TestApp
>>> import jsonrpc2

addメソッドで、RPCメソッドを追加します。

>>> app = jsonrpc2.JsonRpcApplication()
>>> app.add('hello', lambda n: "Hello, %s!" % n)
>>> app = TestApp(app)
>>> res = app.post('/', '{"jsonrpc":"2.0", "method":"hello", "params":["aodag"], "id":"x"}', extra_environ={'CONTENT_TYPE':'application/json'})
>>> res.status_int
200
>>> res.json['id']
'x'
>>> res.json["result"]
'Hello, aodag!'


モジュール単位で追加可能です。
tests.sample.py::

  def greeting(n):
      return "Hello, %s" % n


>>> import tests.sample
>>> app = jsonrpc2.JsonRpcApplication()
>>> app.addModule(tests.sample)
>>> app = TestApp(app)
>>> res = app.post('/', '{"jsonrpc":"2.0", "method":"tests.sample.greeting", "params":["aodag"], "id":"y"}', extra_environ={'CONTENT_TYPE':'application/json'})
>>> res.status_int
200
>>> res.json['id']
'y'
>>> res.json["result"]
'Hello, aodag'

