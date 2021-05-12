import xmlrpclib
from spyne import Application, rpc, ServiceBase, \
    Integer, Unicode
from spyne import Iterable
from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication



class HelloWorldService(ServiceBase):




    @rpc(Unicode, _returns=Unicode)
    def say_hello(ctx, arg):
        a=name
        yield 'Hello, %s' % name



application = Application([HelloWorldService],
    tns='spyne.examples.hello',
    in_protocol=Soap11(),
    out_protocol=Soap11()
)




if __name__ == '__main__':
    from wsgiref.simple_server import make_server
    wsgi_app = WsgiApplication(application)
    server = make_server('127.0.0.1', 8000, wsgi_app)
    server.serve_forever()

proxy = xmlrpclib.ServerProxy("http://localhost:9000/RPC2")

print proxy.printHex("0x01")