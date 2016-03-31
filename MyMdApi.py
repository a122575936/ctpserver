import logging
import Queue
import time
from ctp.futures import MdApi,ApiStruct
from blinker import signal

class MyMdApi(MdApi):
    def __init__(self):
        self.log = logging.getLogger("MyMdApi")
        self.queue = Queue.PriorityQueue()
        self.requestID = 1
        self.BrokerID = "8000"
        self.InvestorID = "81180429"

    def run(self):
        while not self.queue.empty():
            func = self.queue.get()
            apply(func[1])
            time.sleep(1)

    def OnFrontConnected(self):
        self.log.debug("OnFrontConnected")
        signal("OnFrontConnected").send(self)

    def OnFrontDisconnected(self, nReason):
        self.log.debug("OnFrontDisconnected")
        self.log.debug(nReason)
        signal("OnFrontDisconnected").send(self, nReason = nReason)

    def OnHeartBeatWarning(self, nTimeLapse):
        self.log.debug("OnHeartBeatWarning")
        self.log.debug(nTimeLapse)
        signal("OnHeartBeatWarning").send(self, nTimeLapse = nTimeLapse)

    def OnRspError(self, pRspInfo, nRequestID, bIsLast):
        self.log.debug("OnRspError")
        self.log.debug(pRspInfo)
        self.log.debug(nRequestID)
        self.log.debug(bIsLast)
        signal("OnRspError").send(self, pRspInfo = pRspInfo, nRequestID = nRequestID, bIsLast = bIsLast)

    def OnRspSubMarketData(self, pSpecificInstrument, pRspInfo, nRequestID, bIsLast):
        self.log.debug("OnRspSubMarketData")
        self.log.debug(pSpecificInstrument)
        self.log.debug(pRspInfo)
        self.log.debug(nRequestID)
        self.log.debug(bIsLast)
        signal("OnRspSubMarketData").send(self, pSpecificInstrument = pSpecificInstrument, pRspInfo = pRspInfo, nRequestID = nRequestID, bIsLast = bIsLast)

    def OnRspUnSubMarketData(self, pSpecificInstrument, pRspInfo, nRequestID, bIsLast):
        self.log.debug("OnRspUnSubMarketData")
        self.log.debug(pSpecificInstrument)
        self.log.debug(pRspInfo)
        self.log.debug(nRequestID)
        self.log.debug(bIsLast)
        signal("OnRspUnSubMarketData").send(self, pSpecificInstrument = pSpecificInstrument, pRspInfo = pRspInfo, nRequestID = nRequestID, bIsLast = bIsLast)

    def OnRspUserLogin(self, pRspUserLogin, pRspInfo, nRequestID, bIsLast):
        self.log.debug("OnRspUserLogin")
        self.log.debug(pRspUserLogin)
        self.log.debug(pRspInfo)
        self.log.debug(nRequestID)
        self.log.debug(bIsLast)
        signal("OnRspUserLogin").send(self, pRspUserLogin = pRspUserLogin, pRspInfo = pRspInfo, nRequestID = nRequestID, bIsLast = bIsLast)

    def OnRspUserLogout(self, pUserLogout, pRspInfo, nRequestID, bIsLast):
        self.log.debug("OnRspUserLogout")
        self.log.debug(pUserLogout)
        self.log.debug(pRspInfo)
        self.log.debug(nRequestID)
        self.log.debug(bIsLast)
        signal("OnRspUserLogout").send(self, pUserLogout = pUserLogout, pRspInfo = pRspInfo, nRequestID = nRequestID, bIsLast = bIsLast)

    def OnRtnDepthMarketData(self, pDepthMarketData):
        self.log.debug("OnRtnDepthMarketData")
        self.log.debug(pDepthMarketData)
        signal("OnRtnDepthMarketData").send(self, pDepthMarketData = pDepthMarketData)
    def myReqUserLogin(self, *args, **kwargs):
        self.log.debug("myReqUserLogin")
        self.requestID += 1
        requestID = self.requestID
        pReqUserLogin = ApiStruct.ReqUserLogin(**kwargs)
        pReqUserLogin.BrokerID = self.BrokerID
        pReqUserLogin.InvestorID= self.InvestorID
        self.queue.put((1000, lambda :self.ReqUserLogin(pReqUserLogin, requestID)))
        self.run()

    def myReqUserLogout(self, *args, **kwargs):
        self.log.debug("myReqUserLogout")
        self.requestID += 1
        requestID = self.requestID
        pUserLogout = ApiStruct.UserLogout(**kwargs)
        pUserLogout.BrokerID = self.BrokerID
        pUserLogout.InvestorID= self.InvestorID
        self.queue.put((1000, lambda :self.ReqUserLogout(pUserLogout, requestID)))
        self.run()

