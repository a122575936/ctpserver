from __init__ import TraderApi
import inspect


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
    ret += 'from ctp.futures import TraderApi,ApiStruct\n'
    ret += 'from blinker import signal\n'
    ret += "class MyTraderApi(TraderApi):\n"
    ret += '    def __init__(self):\n'
    ret += '        self.log = logging.getLogger("MyTraderApi")\n'
    ret += '        self.requestID = 1\n'
    ret += '        self.BrokerID = "8000"\n'
    ret += '        self.InvestorID = "81180429"\n'
    for k in dir(obj):
        attr = getattr(obj, k)
        if k.startswith('On'):
            #print(type(attr), k)
            #print(attr.__func__)
            funcname = attr.__func__.__name__
            # print(funcname)
            args = inspect.getargspec(attr.__func__).args
            ret += '\n'
            #print(inspect.getargspec(attr.__func__))
            ret += '    def %s(%s):\n' % (funcname, ', '.join(args))
            ret += '        self.log.debug("%s")\n' % (funcname)
            for a in args[1:]:
                ret += '        self.log.debug(%s)\n' % (a)
            if len(args) > 1:
                ret += '        signal("%s").send(self, %s)\n' % (funcname, ', '.join(map(lambda a: '%s = %s' % (a, a), args[1:])))
            else:
                ret += '        signal("%s").send(self)\n' % (funcname)

            #print(dir(attr))
        if k.startswith('Req'):
            funcname = attr.__func__.__name__
            arg1 = inspect.getargspec(attr.__func__).args[1]
            fn = 'my' + funcname
            ret += '    def %s(self, *args, **kwargs):\n' % (fn)
            ret += '        self.log.debug("%s")\n' % (fn)
            ret += '        self.requestID += 1\n'
            ret += '        %s = ApiStruct.%s(%s)\n' % (arg1, arg1[1:], '**kwargs')
            ret += '        %s.BrokerID = self.BrokerID\n' % (arg1)
            ret += '        %s.InvestorID= self.InvestorID\n' % (arg1)
            ret += '        self.%s(%s, self.requestID)\n' % (funcname, arg1)
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
