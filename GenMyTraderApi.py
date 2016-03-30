from __init__ import TraderApi
from paop import Aspect
import inspect

class MyAspect(Aspect):
	def on_enter(self, call):
		print("on enter: ", call.args, call.func.__name__)
        #print(call.func.__name__)
		
	def on_success(self, call):
		print "on success: ", call.result
		
	def on_fail(self, call):
		print "on fail: ", call.exception

def person_say(*args, **kwargs):
    print('rewrite say ', args, kwargs)

@MyAspect()
class Persion(object):
    def __init__(self, name):
        self.name = name

    def say(self, str):
        print(str)

def inspectobject(obj):
    for k in dir(obj):
        attr = getattr(obj, k)
        if k.startswith('On'):
            #print(type(attr), k)
            #print(attr.__func__)
            print(inspect.getargspec(attr.__func__))
            #print(dir(attr))
        if k.startswith('Req'):
            #print(type(attr), k)
            #print(dir(attr))
            print(inspect.getargspec(attr.__func__))

def genTraderSpi(obj):
    ret = 'import logging\n'
    ret += "class MyTraderApi(TraderApi):\n"
    ret += '    def __init__(self):\n'
    ret += '        self.log = logging.getlogger("MyTraderApi")\n'
    for k in dir(obj):
        attr = getattr(obj, k)
        if k.startswith('On'):
            #print(type(attr), k)
            #print(attr.__func__)
            ret += '\n'
            #print(inspect.getargspec(attr.__func__))
            ret += '    def %s(%s):\n' % (attr.__func__.__name__, ', '.join(inspect.getargspec(attr.__func__).args))
            ret += '        log.debug("%s", %s)\n' % (attr.__func__.__name__, ', '.join(inspect.getargspec(attr.__func__).args[1:]))
            #print(dir(attr))
        if k.startswith('Req'):
            funcname = attr.__func__.__name__
            arg1 = inspect.getargspec(attr.__func__).args[1]
            fn = 'my' + funcname
            ret += '    def %s(self, *args, **kwargs):\n' % (fn)
            ret += '        log.debug("%s")\n' % (fn)
            ret += '        self.requestID++\n'
            ret += '        %s = ApiStruct.%s(%s)\n' % (arg1, arg1[1:], '**kwargs')
            ret += '        %s.BrokerID = self.BrokerID\n' % (arg1)
            ret += '        %s.InvestorID= self.InvestorID\n' % (arg1)
            ret += '        self.%s(%s, self.requestID):\n' % (funcname, arg1)
            ret += '\n'
    print(ret)
    with open('MyTraderApi.py', 'w') as f:
        f.write(ret)


def main():
    #inspectobject(TraderApi)
    #api = TraderApi()
    #inspectobject(api)

    genTraderSpi(TraderApi())

    #p = Persion('liyiyi')
    #p.say('hello')
    #print(p.name)

    #print(dir(Persion))

main()
