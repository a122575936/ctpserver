from __init__ import TraderApi, MdApi
import inspect

def genSpi(obj):
    classname = obj.__class__.__name__
    myclassname = 'My' + classname
    ret = 'import logging\n'
    ret += 'import Queue\n'
    ret += 'import time\n'
    ret += 'from ctp.futures import %s,ApiStruct\n' % (classname)
    ret += 'from blinker import signal\n\n'
    ret += "class %s(%s):\n" % (myclassname, classname)
    ret += '    def __init__(self):\n'
    ret += '        self.log = logging.getLogger("%s")\n' % (myclassname)
    ret += '        self.queue = Queue.PriorityQueue()\n'
    ret += '        self.requestID = 1\n'
    ret += '        self.BrokerID = "8000"\n'
    ret += '        self.InvestorID = "81180429"\n\n'
    ret += '    def run(self):\n'
    ret += '        while not self.queue.empty():\n'
    ret += '            func = self.queue.get()\n'
    ret += '            apply(func[1])\n'
    ret += '            time.sleep(1)\n'
    for k in dir(obj):
        attr = getattr(obj, k)
        if k.startswith('On'):
            funcname = attr.__func__.__name__
            args = inspect.getargspec(attr.__func__).args
            ret += '\n'
            ret += '    def %s(%s):\n' % (funcname, ', '.join(args))
            ret += '        self.log.debug("%s")\n' % (funcname)
            for a in args[1:]:
                ret += '        self.log.debug(%s)\n' % (a)
            if len(args) > 1:
                ret += '        signal("%s").send(self, %s)\n' % (funcname, ', '.join(map(lambda a: '%s = %s' % (a, a), args[1:])))
            else:
                ret += '        signal("%s").send(self)\n' % (funcname)

        if k.startswith('Req'):
            funcname = attr.__func__.__name__
            arg1 = inspect.getargspec(attr.__func__).args[1]
            fn = 'my' + funcname
            ret += '    def %s(self, *args, **kwargs):\n' % (fn)
            ret += '        self.log.debug("%s")\n' % (fn)
            ret += '        self.requestID += 1\n'
            ret += '        requestID = self.requestID\n'
            ret += '        %s = ApiStruct.%s(%s)\n' % (arg1, arg1[1:], '**kwargs')
            ret += '        %s.BrokerID = self.BrokerID\n' % (arg1)
            ret += '        %s.InvestorID= self.InvestorID\n' % (arg1)
            ret += '        self.queue.put((1000, lambda :self.%s(%s, requestID)))\n' % (funcname, arg1)
            ret += '        self.run()\n'
            ret += '\n'
    #print(ret)
    with open('%s.py' % (myclassname), 'w') as f:
        f.write(ret)

def main():
    genSpi(TraderApi())
    genSpi(MdApi())

main()
