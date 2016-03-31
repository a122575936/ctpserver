#!/usr/bin/env python

import sys, glob, logging, config
sys.path.append('gen-py')
# sys.path.insert(0, glob.glob('../../lib/py/build/lib.*')[0])

from trader import Trader
from MyTraderApi import MyTraderApi
from blinker import signal

from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
from thrift.server import TServer

logging.basicConfig(level=logging.DEBUG,
        format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
        datefmt='%a, %d %b %Y %H:%M:%S',
        filename='trader.txt',
        filemode='w')

class TraderHandler:
  def __init__(self):
    signal('OnFrontConnected').connect(self.OnFrontConnected)
    signal('OnRtnTradingNotice').connect(self.OnRtnTradingNotice)
    signal('OnRtnOrder').connect(self.OnRtnOrder)
    signal('OnRspQryInvestorPositionDetail').connect(self.OnRspQryInvestorPositionDetail)
    self.traderapi = MyTraderApi()
    self.traderapi.Create()
    self.traderapi.RegisterFront('tcp://180.168.212.75:41205')
    self.traderapi.Init()

  def ping(self):
    print 'ping()'

  def check(self, contract, ordertype):
    print 'check(%s,%s)' % (contract, ordertype)

  def OnFrontConnected(self, sender, **kwargs):
    self.traderapi.myReqUserLogin(UserID = config.UserID, Password = config.Password)
    self.traderapi.myReqQryInvestorPositionDetail()

  def OnRtnTradingNotice(self, sender, **kwargs):
    print(kwargs['pTradingNoticeInfo'].FieldContent.decode('gbk'))

  def OnRspQryInvestorPositionDetail(self, sender, **kwargs):
    pass

  def OnRtnOrder(self, sender, **kwargs):
    pOrder = kwargs['pOrder']
    print('OnRtnOrder %s %s' % (pOrder.InstrumentID, pOrder.StatusMsg.decode('gbk')))

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
