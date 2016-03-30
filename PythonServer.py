#!/usr/bin/env python

import sys, glob
sys.path.append('gen-py')
# sys.path.insert(0, glob.glob('../../lib/py/build/lib.*')[0])

from trader import Trader
from MyTraderApi import MyTraderApi

from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
from thrift.server import TServer

class TraderHandler:
  def __init__(self):
    self.traderapi = MyTraderApi()
    self.traderapi.Create()
    self.traderapi.RegisterFront('tcp://180.168.212.75:41205')
    self.traderapi.Init()

  def ping(self):
    print 'ping()'

  def check(self, contract, ordertype):
    print 'check(%s,%s)' % (contract, ordertype)

handler = TraderHandler()
processor = Trader.Processor(handler)
transport = TSocket.TServerSocket(port=9090)
tfactory = TTransport.TBufferedTransportFactory()
pfactory = TBinaryProtocol.TBinaryProtocolFactory()

server = TServer.TSimpleServer(processor, transport, tfactory, pfactory)

# You could do one of these for a multithreaded server
#server = TServer.TThreadedServer(processor, transport, tfactory, pfactory)
#server = TServer.TThreadPoolServer(processor, transport, tfactory, pfactory)

print 'Starting the server...'
server.serve()
print 'done.'
