#!/usr/bin/env python

import sys, glob, logging, config
sys.path.append('gen-py')
# sys.path.insert(0, glob.glob('../../lib/py/build/lib.*')[0])

from trader import Trader
from MyTraderApi import MyTraderApi
from blinker import signal
from ctp.futures import ApiStruct

from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TJSONProtocol
from thrift.server import THttpServer

logging.basicConfig(level=logging.DEBUG,
        format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
        datefmt='%a, %d %b %Y %H:%M:%S',
        filename='trader.txt',
        filemode='w')

def evalApiStruct(str):
    return eval('ApiStruct.' + str)

class TraderHandler:
    def __init__(self):
        signal('OnFrontConnected').connect(self.OnFrontConnected)
        signal('OnRspUserLogin').connect(self.OnRspUserLogin)
        #signal('OnRtnInstrumentStatus').connect(self.OnRtnInstrumentStatus)
        signal('OnRtnTradingNotice').connect(self.OnRtnTradingNotice)
        signal('OnRtnOrder').connect(self.OnRtnOrder)
        signal('OnRtnTrade').connect(self.OnRtnTrade)
        signal('OnRspQryDepthMarketData').connect(self.OnRspQryDepthMarketData)
        signal('OnRspQryInvestorPosition').connect(self.OnRspQryInvestorPosition)
        signal('OnRspQryInvestorPositionDetail').connect(self.OnRspQryInvestorPositionDetail)
        self.traderapi = MyTraderApi()
        self.traderapi.Create()
        self.traderapi.RegisterFront('tcp://180.168.212.75:41205')
        self.traderapi.Init()
        self.investorPositions = []
        self.depthMarketDataDict = {}

    def ping(self):
        print 'ping()'

    def check(self, contract, ordertype):
        logging.debug('check(%s,%s)' % (contract, ordertype))
        for position in self.investorPositions:
            instrument = position.InstrumentID.upper()
            if contract != instrument:
                continue
            if position.Position > 0:
                pDepthMarketData = self.depthMarketDataDict.get(position.InstrumentID, None)
                if not pDepthMarketData:
                    continue
                if position.PosiDirection == ApiStruct.PD_Long and ordertype == 'sell':
                    logging.debug('check long close %s', pDepthMarketData.LowerLimitPrice)
                    self.reqOrderInsert(position.InstrumentID, ApiStruct.D_Sell, ApiStruct.OF_Close, pDepthMarketData.LowerLimitPrice, position.Position)
                elif position.PosiDirection == ApiStruct.PD_Short and ordertype == 'buy':
                    logging.debug('check short close %s', pDepthMarketData.UpperLimitPrice)
                    self.reqOrderInsert(position.InstrumentID, ApiStruct.D_Buy, ApiStruct.OF_Close, pDepthMarketData.UpperLimitPrice, position.Position)

    def reqOrderInsert(self, instrumentID, dir, combOffsetFlag, price, volume):
        self.traderapi.myReqOrderInsert(
                InstrumentID = instrumentID,
                OrderRef = str(self.traderapi.requestID),
                UserID = config.UserID,
                OrderPriceType = ApiStruct.OPT_LimitPrice,
                Direction = dir,
                CombOffsetFlag = combOffsetFlag,
                CombHedgeFlag = '1',
                LimitPrice = price,
                VolumeTotalOriginal = volume,
                TimeCondition = ApiStruct.TC_GFD,
                GTDDate = '',
                VolumeCondition = ApiStruct.VC_AV,
                MinVolume = 0,
                ContingentCondition = ApiStruct.CC_Immediately,
                StopPrice = 0,
                ForceCloseReason = ApiStruct.FCC_NotForceClose,
                IsAutoSuspend = 0,
                )

    def OnRspUserLogin(self, sender, **kwargs):
        #self.investorPositions = []
        #self.traderapi.myReqQryInvestorPosition()
        pass

    def OnFrontConnected(self, sender, **kwargs):
        self.traderapi.myReqUserLogin(UserID = config.UserID, Password = config.Password)
        self.traderapi.myReqQryDepthMarketData()
        self.investorPositions = []
        self.traderapi.myReqQryInvestorPosition()

    def OnRtnTradingNotice(self, sender, **kwargs):
        print(kwargs['pTradingNoticeInfo'].FieldContent.decode('gbk'))

    def OnRspQryInvestorPosition(self, sender, **kwargs):
        pInvestorPosition = kwargs['pInvestorPosition']
        bIsLast = kwargs['bIsLast']
        self.investorPositions.append(evalApiStruct(pInvestorPosition.__str__()))

    def OnRspQryInvestorPositionDetail(self, sender, **kwargs):
        pass

    def OnRspQryDepthMarketData(self, sender, **kwargs):
        pDepthMarketData = kwargs['pDepthMarketData']
        self.depthMarketDataDict[pDepthMarketData.InstrumentID] = evalApiStruct(pDepthMarketData.__str__())

    def OnRtnTrade(self, sender, **kwargs):
        #self.investorPositions = []
        #self.traderapi.myReqQryInvestorPosition()
        pass

    def OnRtnOrder(self, sender, **kwargs):
        pOrder = kwargs['pOrder']
        print('OnRtnOrder %s %s' % (pOrder.InstrumentID, pOrder.StatusMsg.decode('gbk')))

def StartServer():
    handler = TraderHandler()
    processor = Trader.Processor(handler)
    transport = TSocket.TServerSocket(port=9090)
    tfactory = TTransport.TBufferedTransportFactory()
    pfactory = TJSONProtocol.TJSONProtocolFactory()

    server = THttpServer.THttpServer(processor, ('127.0.0.1', 8000), pfactory, pfactory)

    # You could do one of these for a multithreaded server
    #server = TServer.TThreadedServer(processor, transport, tfactory, pfactory)
    #server = TServer.TThreadPoolServer(processor, transport, tfactory, pfactory)

    print 'Starting the server...'
    server.serve()
    print 'done.'

if __name__ == '__main__':
    StartServer()
