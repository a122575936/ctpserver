import logging
import Queue
import time
from ctp.futures import TraderApi,ApiStruct
from blinker import signal

from call_repeatedly import call_repeatedly

class MyTraderApi(TraderApi):
    def __init__(self):
        self.log = logging.getLogger("MyTraderApi")
        self.queue = Queue.PriorityQueue()
        self.requestID = 1
        call_repeatedly(1, self.run)
        self.BrokerID = "8000"
        self.InvestorID = "81180429"

    def run(self):
        if not self.queue.empty():
            func = self.queue.get()
            apply(func[1])

    def OnErrRtnBankToFutureByFuture(self, pReqTransfer, pRspInfo):
        self.log.debug("OnErrRtnBankToFutureByFuture")
        self.log.debug(pReqTransfer)
        self.log.debug(pRspInfo)
        signal("OnErrRtnBankToFutureByFuture").send(self, pReqTransfer = pReqTransfer, pRspInfo = pRspInfo)

    def OnErrRtnFutureToBankByFuture(self, pReqTransfer, pRspInfo):
        self.log.debug("OnErrRtnFutureToBankByFuture")
        self.log.debug(pReqTransfer)
        self.log.debug(pRspInfo)
        signal("OnErrRtnFutureToBankByFuture").send(self, pReqTransfer = pReqTransfer, pRspInfo = pRspInfo)

    def OnErrRtnOrderAction(self, pOrderAction, pRspInfo):
        self.log.debug("OnErrRtnOrderAction")
        self.log.debug(pOrderAction)
        self.log.debug(pRspInfo)
        signal("OnErrRtnOrderAction").send(self, pOrderAction = pOrderAction, pRspInfo = pRspInfo)

    def OnErrRtnOrderInsert(self, pInputOrder, pRspInfo):
        self.log.debug("OnErrRtnOrderInsert")
        self.log.debug(pInputOrder)
        self.log.debug(pRspInfo)
        signal("OnErrRtnOrderInsert").send(self, pInputOrder = pInputOrder, pRspInfo = pRspInfo)

    def OnErrRtnQueryBankBalanceByFuture(self, pReqQueryAccount, pRspInfo):
        self.log.debug("OnErrRtnQueryBankBalanceByFuture")
        self.log.debug(pReqQueryAccount)
        self.log.debug(pRspInfo)
        signal("OnErrRtnQueryBankBalanceByFuture").send(self, pReqQueryAccount = pReqQueryAccount, pRspInfo = pRspInfo)

    def OnErrRtnRepealBankToFutureByFutureManual(self, pReqRepeal, pRspInfo):
        self.log.debug("OnErrRtnRepealBankToFutureByFutureManual")
        self.log.debug(pReqRepeal)
        self.log.debug(pRspInfo)
        signal("OnErrRtnRepealBankToFutureByFutureManual").send(self, pReqRepeal = pReqRepeal, pRspInfo = pRspInfo)

    def OnErrRtnRepealFutureToBankByFutureManual(self, pReqRepeal, pRspInfo):
        self.log.debug("OnErrRtnRepealFutureToBankByFutureManual")
        self.log.debug(pReqRepeal)
        self.log.debug(pRspInfo)
        signal("OnErrRtnRepealFutureToBankByFutureManual").send(self, pReqRepeal = pReqRepeal, pRspInfo = pRspInfo)

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

    def OnRspAuthenticate(self, pRspAuthenticate, pRspInfo, nRequestID, bIsLast):
        self.log.debug("OnRspAuthenticate")
        self.log.debug(pRspAuthenticate)
        self.log.debug(pRspInfo)
        self.log.debug(nRequestID)
        self.log.debug(bIsLast)
        signal("OnRspAuthenticate").send(self, pRspAuthenticate = pRspAuthenticate, pRspInfo = pRspInfo, nRequestID = nRequestID, bIsLast = bIsLast)

    def OnRspError(self, pRspInfo, nRequestID, bIsLast):
        self.log.debug("OnRspError")
        self.log.debug(pRspInfo)
        self.log.debug(nRequestID)
        self.log.debug(bIsLast)
        signal("OnRspError").send(self, pRspInfo = pRspInfo, nRequestID = nRequestID, bIsLast = bIsLast)

    def OnRspFromBankToFutureByFuture(self, pReqTransfer, pRspInfo, nRequestID, bIsLast):
        self.log.debug("OnRspFromBankToFutureByFuture")
        self.log.debug(pReqTransfer)
        self.log.debug(pRspInfo)
        self.log.debug(nRequestID)
        self.log.debug(bIsLast)
        signal("OnRspFromBankToFutureByFuture").send(self, pReqTransfer = pReqTransfer, pRspInfo = pRspInfo, nRequestID = nRequestID, bIsLast = bIsLast)

    def OnRspFromFutureToBankByFuture(self, pReqTransfer, pRspInfo, nRequestID, bIsLast):
        self.log.debug("OnRspFromFutureToBankByFuture")
        self.log.debug(pReqTransfer)
        self.log.debug(pRspInfo)
        self.log.debug(nRequestID)
        self.log.debug(bIsLast)
        signal("OnRspFromFutureToBankByFuture").send(self, pReqTransfer = pReqTransfer, pRspInfo = pRspInfo, nRequestID = nRequestID, bIsLast = bIsLast)

    def OnRspOrderAction(self, pInputOrderAction, pRspInfo, nRequestID, bIsLast):
        self.log.debug("OnRspOrderAction")
        self.log.debug(pInputOrderAction)
        self.log.debug(pRspInfo)
        self.log.debug(nRequestID)
        self.log.debug(bIsLast)
        signal("OnRspOrderAction").send(self, pInputOrderAction = pInputOrderAction, pRspInfo = pRspInfo, nRequestID = nRequestID, bIsLast = bIsLast)

    def OnRspOrderInsert(self, pInputOrder, pRspInfo, nRequestID, bIsLast):
        self.log.debug("OnRspOrderInsert")
        self.log.debug(pInputOrder)
        self.log.debug(pRspInfo)
        self.log.debug(nRequestID)
        self.log.debug(bIsLast)
        signal("OnRspOrderInsert").send(self, pInputOrder = pInputOrder, pRspInfo = pRspInfo, nRequestID = nRequestID, bIsLast = bIsLast)

    def OnRspParkedOrderAction(self, pParkedOrderAction, pRspInfo, nRequestID, bIsLast):
        self.log.debug("OnRspParkedOrderAction")
        self.log.debug(pParkedOrderAction)
        self.log.debug(pRspInfo)
        self.log.debug(nRequestID)
        self.log.debug(bIsLast)
        signal("OnRspParkedOrderAction").send(self, pParkedOrderAction = pParkedOrderAction, pRspInfo = pRspInfo, nRequestID = nRequestID, bIsLast = bIsLast)

    def OnRspParkedOrderInsert(self, pParkedOrder, pRspInfo, nRequestID, bIsLast):
        self.log.debug("OnRspParkedOrderInsert")
        self.log.debug(pParkedOrder)
        self.log.debug(pRspInfo)
        self.log.debug(nRequestID)
        self.log.debug(bIsLast)
        signal("OnRspParkedOrderInsert").send(self, pParkedOrder = pParkedOrder, pRspInfo = pRspInfo, nRequestID = nRequestID, bIsLast = bIsLast)

    def OnRspQryAccountregister(self, pAccountregister, pRspInfo, nRequestID, bIsLast):
        self.log.debug("OnRspQryAccountregister")
        self.log.debug(pAccountregister)
        self.log.debug(pRspInfo)
        self.log.debug(nRequestID)
        self.log.debug(bIsLast)
        signal("OnRspQryAccountregister").send(self, pAccountregister = pAccountregister, pRspInfo = pRspInfo, nRequestID = nRequestID, bIsLast = bIsLast)

    def OnRspQryBrokerTradingAlgos(self, pBrokerTradingAlgos, pRspInfo, nRequestID, bIsLast):
        self.log.debug("OnRspQryBrokerTradingAlgos")
        self.log.debug(pBrokerTradingAlgos)
        self.log.debug(pRspInfo)
        self.log.debug(nRequestID)
        self.log.debug(bIsLast)
        signal("OnRspQryBrokerTradingAlgos").send(self, pBrokerTradingAlgos = pBrokerTradingAlgos, pRspInfo = pRspInfo, nRequestID = nRequestID, bIsLast = bIsLast)

    def OnRspQryBrokerTradingParams(self, pBrokerTradingParams, pRspInfo, nRequestID, bIsLast):
        self.log.debug("OnRspQryBrokerTradingParams")
        self.log.debug(pBrokerTradingParams)
        self.log.debug(pRspInfo)
        self.log.debug(nRequestID)
        self.log.debug(bIsLast)
        signal("OnRspQryBrokerTradingParams").send(self, pBrokerTradingParams = pBrokerTradingParams, pRspInfo = pRspInfo, nRequestID = nRequestID, bIsLast = bIsLast)

    def OnRspQryCFMMCTradingAccountKey(self, pCFMMCTradingAccountKey, pRspInfo, nRequestID, bIsLast):
        self.log.debug("OnRspQryCFMMCTradingAccountKey")
        self.log.debug(pCFMMCTradingAccountKey)
        self.log.debug(pRspInfo)
        self.log.debug(nRequestID)
        self.log.debug(bIsLast)
        signal("OnRspQryCFMMCTradingAccountKey").send(self, pCFMMCTradingAccountKey = pCFMMCTradingAccountKey, pRspInfo = pRspInfo, nRequestID = nRequestID, bIsLast = bIsLast)

    def OnRspQryContractBank(self, pContractBank, pRspInfo, nRequestID, bIsLast):
        self.log.debug("OnRspQryContractBank")
        self.log.debug(pContractBank)
        self.log.debug(pRspInfo)
        self.log.debug(nRequestID)
        self.log.debug(bIsLast)
        signal("OnRspQryContractBank").send(self, pContractBank = pContractBank, pRspInfo = pRspInfo, nRequestID = nRequestID, bIsLast = bIsLast)

    def OnRspQryDepthMarketData(self, pDepthMarketData, pRspInfo, nRequestID, bIsLast):
        self.log.debug("OnRspQryDepthMarketData")
        self.log.debug(pDepthMarketData)
        self.log.debug(pRspInfo)
        self.log.debug(nRequestID)
        self.log.debug(bIsLast)
        signal("OnRspQryDepthMarketData").send(self, pDepthMarketData = pDepthMarketData, pRspInfo = pRspInfo, nRequestID = nRequestID, bIsLast = bIsLast)

    def OnRspQryEWarrantOffset(self, pEWarrantOffset, pRspInfo, nRequestID, bIsLast):
        self.log.debug("OnRspQryEWarrantOffset")
        self.log.debug(pEWarrantOffset)
        self.log.debug(pRspInfo)
        self.log.debug(nRequestID)
        self.log.debug(bIsLast)
        signal("OnRspQryEWarrantOffset").send(self, pEWarrantOffset = pEWarrantOffset, pRspInfo = pRspInfo, nRequestID = nRequestID, bIsLast = bIsLast)

    def OnRspQryExchange(self, pExchange, pRspInfo, nRequestID, bIsLast):
        self.log.debug("OnRspQryExchange")
        self.log.debug(pExchange)
        self.log.debug(pRspInfo)
        self.log.debug(nRequestID)
        self.log.debug(bIsLast)
        signal("OnRspQryExchange").send(self, pExchange = pExchange, pRspInfo = pRspInfo, nRequestID = nRequestID, bIsLast = bIsLast)

    def OnRspQryExchangeMarginRate(self, pExchangeMarginRate, pRspInfo, nRequestID, bIsLast):
        self.log.debug("OnRspQryExchangeMarginRate")
        self.log.debug(pExchangeMarginRate)
        self.log.debug(pRspInfo)
        self.log.debug(nRequestID)
        self.log.debug(bIsLast)
        signal("OnRspQryExchangeMarginRate").send(self, pExchangeMarginRate = pExchangeMarginRate, pRspInfo = pRspInfo, nRequestID = nRequestID, bIsLast = bIsLast)

    def OnRspQryExchangeMarginRateAdjust(self, pExchangeMarginRateAdjust, pRspInfo, nRequestID, bIsLast):
        self.log.debug("OnRspQryExchangeMarginRateAdjust")
        self.log.debug(pExchangeMarginRateAdjust)
        self.log.debug(pRspInfo)
        self.log.debug(nRequestID)
        self.log.debug(bIsLast)
        signal("OnRspQryExchangeMarginRateAdjust").send(self, pExchangeMarginRateAdjust = pExchangeMarginRateAdjust, pRspInfo = pRspInfo, nRequestID = nRequestID, bIsLast = bIsLast)

    def OnRspQryExchangeRate(self, pExchangeRate, pRspInfo, nRequestID, bIsLast):
        self.log.debug("OnRspQryExchangeRate")
        self.log.debug(pExchangeRate)
        self.log.debug(pRspInfo)
        self.log.debug(nRequestID)
        self.log.debug(bIsLast)
        signal("OnRspQryExchangeRate").send(self, pExchangeRate = pExchangeRate, pRspInfo = pRspInfo, nRequestID = nRequestID, bIsLast = bIsLast)

    def OnRspQryInstrument(self, pInstrument, pRspInfo, nRequestID, bIsLast):
        self.log.debug("OnRspQryInstrument")
        self.log.debug(pInstrument)
        self.log.debug(pRspInfo)
        self.log.debug(nRequestID)
        self.log.debug(bIsLast)
        signal("OnRspQryInstrument").send(self, pInstrument = pInstrument, pRspInfo = pRspInfo, nRequestID = nRequestID, bIsLast = bIsLast)

    def OnRspQryInstrumentCommissionRate(self, pInstrumentCommissionRate, pRspInfo, nRequestID, bIsLast):
        self.log.debug("OnRspQryInstrumentCommissionRate")
        self.log.debug(pInstrumentCommissionRate)
        self.log.debug(pRspInfo)
        self.log.debug(nRequestID)
        self.log.debug(bIsLast)
        signal("OnRspQryInstrumentCommissionRate").send(self, pInstrumentCommissionRate = pInstrumentCommissionRate, pRspInfo = pRspInfo, nRequestID = nRequestID, bIsLast = bIsLast)

    def OnRspQryInstrumentMarginRate(self, pInstrumentMarginRate, pRspInfo, nRequestID, bIsLast):
        self.log.debug("OnRspQryInstrumentMarginRate")
        self.log.debug(pInstrumentMarginRate)
        self.log.debug(pRspInfo)
        self.log.debug(nRequestID)
        self.log.debug(bIsLast)
        signal("OnRspQryInstrumentMarginRate").send(self, pInstrumentMarginRate = pInstrumentMarginRate, pRspInfo = pRspInfo, nRequestID = nRequestID, bIsLast = bIsLast)

    def OnRspQryInvestor(self, pInvestor, pRspInfo, nRequestID, bIsLast):
        self.log.debug("OnRspQryInvestor")
        self.log.debug(pInvestor)
        self.log.debug(pRspInfo)
        self.log.debug(nRequestID)
        self.log.debug(bIsLast)
        signal("OnRspQryInvestor").send(self, pInvestor = pInvestor, pRspInfo = pRspInfo, nRequestID = nRequestID, bIsLast = bIsLast)

    def OnRspQryInvestorPosition(self, pInvestorPosition, pRspInfo, nRequestID, bIsLast):
        self.log.debug("OnRspQryInvestorPosition")
        self.log.debug(pInvestorPosition)
        self.log.debug(pRspInfo)
        self.log.debug(nRequestID)
        self.log.debug(bIsLast)
        signal("OnRspQryInvestorPosition").send(self, pInvestorPosition = pInvestorPosition, pRspInfo = pRspInfo, nRequestID = nRequestID, bIsLast = bIsLast)

    def OnRspQryInvestorPositionCombineDetail(self, pInvestorPositionCombineDetail, pRspInfo, nRequestID, bIsLast):
        self.log.debug("OnRspQryInvestorPositionCombineDetail")
        self.log.debug(pInvestorPositionCombineDetail)
        self.log.debug(pRspInfo)
        self.log.debug(nRequestID)
        self.log.debug(bIsLast)
        signal("OnRspQryInvestorPositionCombineDetail").send(self, pInvestorPositionCombineDetail = pInvestorPositionCombineDetail, pRspInfo = pRspInfo, nRequestID = nRequestID, bIsLast = bIsLast)

    def OnRspQryInvestorPositionDetail(self, pInvestorPositionDetail, pRspInfo, nRequestID, bIsLast):
        self.log.debug("OnRspQryInvestorPositionDetail")
        self.log.debug(pInvestorPositionDetail)
        self.log.debug(pRspInfo)
        self.log.debug(nRequestID)
        self.log.debug(bIsLast)
        signal("OnRspQryInvestorPositionDetail").send(self, pInvestorPositionDetail = pInvestorPositionDetail, pRspInfo = pRspInfo, nRequestID = nRequestID, bIsLast = bIsLast)

    def OnRspQryInvestorProductGroupMargin(self, pInvestorProductGroupMargin, pRspInfo, nRequestID, bIsLast):
        self.log.debug("OnRspQryInvestorProductGroupMargin")
        self.log.debug(pInvestorProductGroupMargin)
        self.log.debug(pRspInfo)
        self.log.debug(nRequestID)
        self.log.debug(bIsLast)
        signal("OnRspQryInvestorProductGroupMargin").send(self, pInvestorProductGroupMargin = pInvestorProductGroupMargin, pRspInfo = pRspInfo, nRequestID = nRequestID, bIsLast = bIsLast)

    def OnRspQryNotice(self, pNotice, pRspInfo, nRequestID, bIsLast):
        self.log.debug("OnRspQryNotice")
        self.log.debug(pNotice)
        self.log.debug(pRspInfo)
        self.log.debug(nRequestID)
        self.log.debug(bIsLast)
        signal("OnRspQryNotice").send(self, pNotice = pNotice, pRspInfo = pRspInfo, nRequestID = nRequestID, bIsLast = bIsLast)

    def OnRspQryOrder(self, pOrder, pRspInfo, nRequestID, bIsLast):
        self.log.debug("OnRspQryOrder")
        self.log.debug(pOrder)
        self.log.debug(pRspInfo)
        self.log.debug(nRequestID)
        self.log.debug(bIsLast)
        signal("OnRspQryOrder").send(self, pOrder = pOrder, pRspInfo = pRspInfo, nRequestID = nRequestID, bIsLast = bIsLast)

    def OnRspQryParkedOrder(self, pParkedOrder, pRspInfo, nRequestID, bIsLast):
        self.log.debug("OnRspQryParkedOrder")
        self.log.debug(pParkedOrder)
        self.log.debug(pRspInfo)
        self.log.debug(nRequestID)
        self.log.debug(bIsLast)
        signal("OnRspQryParkedOrder").send(self, pParkedOrder = pParkedOrder, pRspInfo = pRspInfo, nRequestID = nRequestID, bIsLast = bIsLast)

    def OnRspQryParkedOrderAction(self, pParkedOrderAction, pRspInfo, nRequestID, bIsLast):
        self.log.debug("OnRspQryParkedOrderAction")
        self.log.debug(pParkedOrderAction)
        self.log.debug(pRspInfo)
        self.log.debug(nRequestID)
        self.log.debug(bIsLast)
        signal("OnRspQryParkedOrderAction").send(self, pParkedOrderAction = pParkedOrderAction, pRspInfo = pRspInfo, nRequestID = nRequestID, bIsLast = bIsLast)

    def OnRspQryProduct(self, pProduct, pRspInfo, nRequestID, bIsLast):
        self.log.debug("OnRspQryProduct")
        self.log.debug(pProduct)
        self.log.debug(pRspInfo)
        self.log.debug(nRequestID)
        self.log.debug(bIsLast)
        signal("OnRspQryProduct").send(self, pProduct = pProduct, pRspInfo = pRspInfo, nRequestID = nRequestID, bIsLast = bIsLast)

    def OnRspQrySecAgentACIDMap(self, pSecAgentACIDMap, pRspInfo, nRequestID, bIsLast):
        self.log.debug("OnRspQrySecAgentACIDMap")
        self.log.debug(pSecAgentACIDMap)
        self.log.debug(pRspInfo)
        self.log.debug(nRequestID)
        self.log.debug(bIsLast)
        signal("OnRspQrySecAgentACIDMap").send(self, pSecAgentACIDMap = pSecAgentACIDMap, pRspInfo = pRspInfo, nRequestID = nRequestID, bIsLast = bIsLast)

    def OnRspQrySettlementInfo(self, pSettlementInfo, pRspInfo, nRequestID, bIsLast):
        self.log.debug("OnRspQrySettlementInfo")
        self.log.debug(pSettlementInfo)
        self.log.debug(pRspInfo)
        self.log.debug(nRequestID)
        self.log.debug(bIsLast)
        signal("OnRspQrySettlementInfo").send(self, pSettlementInfo = pSettlementInfo, pRspInfo = pRspInfo, nRequestID = nRequestID, bIsLast = bIsLast)

    def OnRspQrySettlementInfoConfirm(self, pSettlementInfoConfirm, pRspInfo, nRequestID, bIsLast):
        self.log.debug("OnRspQrySettlementInfoConfirm")
        self.log.debug(pSettlementInfoConfirm)
        self.log.debug(pRspInfo)
        self.log.debug(nRequestID)
        self.log.debug(bIsLast)
        signal("OnRspQrySettlementInfoConfirm").send(self, pSettlementInfoConfirm = pSettlementInfoConfirm, pRspInfo = pRspInfo, nRequestID = nRequestID, bIsLast = bIsLast)

    def OnRspQryTrade(self, pTrade, pRspInfo, nRequestID, bIsLast):
        self.log.debug("OnRspQryTrade")
        self.log.debug(pTrade)
        self.log.debug(pRspInfo)
        self.log.debug(nRequestID)
        self.log.debug(bIsLast)
        signal("OnRspQryTrade").send(self, pTrade = pTrade, pRspInfo = pRspInfo, nRequestID = nRequestID, bIsLast = bIsLast)

    def OnRspQryTradingAccount(self, pTradingAccount, pRspInfo, nRequestID, bIsLast):
        self.log.debug("OnRspQryTradingAccount")
        self.log.debug(pTradingAccount)
        self.log.debug(pRspInfo)
        self.log.debug(nRequestID)
        self.log.debug(bIsLast)
        signal("OnRspQryTradingAccount").send(self, pTradingAccount = pTradingAccount, pRspInfo = pRspInfo, nRequestID = nRequestID, bIsLast = bIsLast)

    def OnRspQryTradingCode(self, pTradingCode, pRspInfo, nRequestID, bIsLast):
        self.log.debug("OnRspQryTradingCode")
        self.log.debug(pTradingCode)
        self.log.debug(pRspInfo)
        self.log.debug(nRequestID)
        self.log.debug(bIsLast)
        signal("OnRspQryTradingCode").send(self, pTradingCode = pTradingCode, pRspInfo = pRspInfo, nRequestID = nRequestID, bIsLast = bIsLast)

    def OnRspQryTradingNotice(self, pTradingNotice, pRspInfo, nRequestID, bIsLast):
        self.log.debug("OnRspQryTradingNotice")
        self.log.debug(pTradingNotice)
        self.log.debug(pRspInfo)
        self.log.debug(nRequestID)
        self.log.debug(bIsLast)
        signal("OnRspQryTradingNotice").send(self, pTradingNotice = pTradingNotice, pRspInfo = pRspInfo, nRequestID = nRequestID, bIsLast = bIsLast)

    def OnRspQryTransferBank(self, pTransferBank, pRspInfo, nRequestID, bIsLast):
        self.log.debug("OnRspQryTransferBank")
        self.log.debug(pTransferBank)
        self.log.debug(pRspInfo)
        self.log.debug(nRequestID)
        self.log.debug(bIsLast)
        signal("OnRspQryTransferBank").send(self, pTransferBank = pTransferBank, pRspInfo = pRspInfo, nRequestID = nRequestID, bIsLast = bIsLast)

    def OnRspQryTransferSerial(self, pTransferSerial, pRspInfo, nRequestID, bIsLast):
        self.log.debug("OnRspQryTransferSerial")
        self.log.debug(pTransferSerial)
        self.log.debug(pRspInfo)
        self.log.debug(nRequestID)
        self.log.debug(bIsLast)
        signal("OnRspQryTransferSerial").send(self, pTransferSerial = pTransferSerial, pRspInfo = pRspInfo, nRequestID = nRequestID, bIsLast = bIsLast)

    def OnRspQueryBankAccountMoneyByFuture(self, pReqQueryAccount, pRspInfo, nRequestID, bIsLast):
        self.log.debug("OnRspQueryBankAccountMoneyByFuture")
        self.log.debug(pReqQueryAccount)
        self.log.debug(pRspInfo)
        self.log.debug(nRequestID)
        self.log.debug(bIsLast)
        signal("OnRspQueryBankAccountMoneyByFuture").send(self, pReqQueryAccount = pReqQueryAccount, pRspInfo = pRspInfo, nRequestID = nRequestID, bIsLast = bIsLast)

    def OnRspQueryCFMMCTradingAccountToken(self, pQueryCFMMCTradingAccountToken, pRspInfo, nRequestID, bIsLast):
        self.log.debug("OnRspQueryCFMMCTradingAccountToken")
        self.log.debug(pQueryCFMMCTradingAccountToken)
        self.log.debug(pRspInfo)
        self.log.debug(nRequestID)
        self.log.debug(bIsLast)
        signal("OnRspQueryCFMMCTradingAccountToken").send(self, pQueryCFMMCTradingAccountToken = pQueryCFMMCTradingAccountToken, pRspInfo = pRspInfo, nRequestID = nRequestID, bIsLast = bIsLast)

    def OnRspQueryMaxOrderVolume(self, pQueryMaxOrderVolume, pRspInfo, nRequestID, bIsLast):
        self.log.debug("OnRspQueryMaxOrderVolume")
        self.log.debug(pQueryMaxOrderVolume)
        self.log.debug(pRspInfo)
        self.log.debug(nRequestID)
        self.log.debug(bIsLast)
        signal("OnRspQueryMaxOrderVolume").send(self, pQueryMaxOrderVolume = pQueryMaxOrderVolume, pRspInfo = pRspInfo, nRequestID = nRequestID, bIsLast = bIsLast)

    def OnRspRemoveParkedOrder(self, pRemoveParkedOrder, pRspInfo, nRequestID, bIsLast):
        self.log.debug("OnRspRemoveParkedOrder")
        self.log.debug(pRemoveParkedOrder)
        self.log.debug(pRspInfo)
        self.log.debug(nRequestID)
        self.log.debug(bIsLast)
        signal("OnRspRemoveParkedOrder").send(self, pRemoveParkedOrder = pRemoveParkedOrder, pRspInfo = pRspInfo, nRequestID = nRequestID, bIsLast = bIsLast)

    def OnRspRemoveParkedOrderAction(self, pRemoveParkedOrderAction, pRspInfo, nRequestID, bIsLast):
        self.log.debug("OnRspRemoveParkedOrderAction")
        self.log.debug(pRemoveParkedOrderAction)
        self.log.debug(pRspInfo)
        self.log.debug(nRequestID)
        self.log.debug(bIsLast)
        signal("OnRspRemoveParkedOrderAction").send(self, pRemoveParkedOrderAction = pRemoveParkedOrderAction, pRspInfo = pRspInfo, nRequestID = nRequestID, bIsLast = bIsLast)

    def OnRspSettlementInfoConfirm(self, pSettlementInfoConfirm, pRspInfo, nRequestID, bIsLast):
        self.log.debug("OnRspSettlementInfoConfirm")
        self.log.debug(pSettlementInfoConfirm)
        self.log.debug(pRspInfo)
        self.log.debug(nRequestID)
        self.log.debug(bIsLast)
        signal("OnRspSettlementInfoConfirm").send(self, pSettlementInfoConfirm = pSettlementInfoConfirm, pRspInfo = pRspInfo, nRequestID = nRequestID, bIsLast = bIsLast)

    def OnRspTradingAccountPasswordUpdate(self, pTradingAccountPasswordUpdate, pRspInfo, nRequestID, bIsLast):
        self.log.debug("OnRspTradingAccountPasswordUpdate")
        self.log.debug(pTradingAccountPasswordUpdate)
        self.log.debug(pRspInfo)
        self.log.debug(nRequestID)
        self.log.debug(bIsLast)
        signal("OnRspTradingAccountPasswordUpdate").send(self, pTradingAccountPasswordUpdate = pTradingAccountPasswordUpdate, pRspInfo = pRspInfo, nRequestID = nRequestID, bIsLast = bIsLast)

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

    def OnRspUserPasswordUpdate(self, pUserPasswordUpdate, pRspInfo, nRequestID, bIsLast):
        self.log.debug("OnRspUserPasswordUpdate")
        self.log.debug(pUserPasswordUpdate)
        self.log.debug(pRspInfo)
        self.log.debug(nRequestID)
        self.log.debug(bIsLast)
        signal("OnRspUserPasswordUpdate").send(self, pUserPasswordUpdate = pUserPasswordUpdate, pRspInfo = pRspInfo, nRequestID = nRequestID, bIsLast = bIsLast)

    def OnRtnCFMMCTradingAccountToken(self, pCFMMCTradingAccountToken):
        self.log.debug("OnRtnCFMMCTradingAccountToken")
        self.log.debug(pCFMMCTradingAccountToken)
        signal("OnRtnCFMMCTradingAccountToken").send(self, pCFMMCTradingAccountToken = pCFMMCTradingAccountToken)

    def OnRtnCancelAccountByBank(self, pCancelAccount):
        self.log.debug("OnRtnCancelAccountByBank")
        self.log.debug(pCancelAccount)
        signal("OnRtnCancelAccountByBank").send(self, pCancelAccount = pCancelAccount)

    def OnRtnChangeAccountByBank(self, pChangeAccount):
        self.log.debug("OnRtnChangeAccountByBank")
        self.log.debug(pChangeAccount)
        signal("OnRtnChangeAccountByBank").send(self, pChangeAccount = pChangeAccount)

    def OnRtnErrorConditionalOrder(self, pErrorConditionalOrder):
        self.log.debug("OnRtnErrorConditionalOrder")
        self.log.debug(pErrorConditionalOrder)
        signal("OnRtnErrorConditionalOrder").send(self, pErrorConditionalOrder = pErrorConditionalOrder)

    def OnRtnFromBankToFutureByBank(self, pRspTransfer):
        self.log.debug("OnRtnFromBankToFutureByBank")
        self.log.debug(pRspTransfer)
        signal("OnRtnFromBankToFutureByBank").send(self, pRspTransfer = pRspTransfer)

    def OnRtnFromBankToFutureByFuture(self, pRspTransfer):
        self.log.debug("OnRtnFromBankToFutureByFuture")
        self.log.debug(pRspTransfer)
        signal("OnRtnFromBankToFutureByFuture").send(self, pRspTransfer = pRspTransfer)

    def OnRtnFromFutureToBankByBank(self, pRspTransfer):
        self.log.debug("OnRtnFromFutureToBankByBank")
        self.log.debug(pRspTransfer)
        signal("OnRtnFromFutureToBankByBank").send(self, pRspTransfer = pRspTransfer)

    def OnRtnFromFutureToBankByFuture(self, pRspTransfer):
        self.log.debug("OnRtnFromFutureToBankByFuture")
        self.log.debug(pRspTransfer)
        signal("OnRtnFromFutureToBankByFuture").send(self, pRspTransfer = pRspTransfer)

    def OnRtnInstrumentStatus(self, pInstrumentStatus):
        self.log.debug("OnRtnInstrumentStatus")
        self.log.debug(pInstrumentStatus)
        signal("OnRtnInstrumentStatus").send(self, pInstrumentStatus = pInstrumentStatus)

    def OnRtnOpenAccountByBank(self, pOpenAccount):
        self.log.debug("OnRtnOpenAccountByBank")
        self.log.debug(pOpenAccount)
        signal("OnRtnOpenAccountByBank").send(self, pOpenAccount = pOpenAccount)

    def OnRtnOrder(self, pOrder):
        self.log.debug("OnRtnOrder")
        self.log.debug(pOrder)
        signal("OnRtnOrder").send(self, pOrder = pOrder)

    def OnRtnQueryBankBalanceByFuture(self, pNotifyQueryAccount):
        self.log.debug("OnRtnQueryBankBalanceByFuture")
        self.log.debug(pNotifyQueryAccount)
        signal("OnRtnQueryBankBalanceByFuture").send(self, pNotifyQueryAccount = pNotifyQueryAccount)

    def OnRtnRepealFromBankToFutureByBank(self, pRspRepeal):
        self.log.debug("OnRtnRepealFromBankToFutureByBank")
        self.log.debug(pRspRepeal)
        signal("OnRtnRepealFromBankToFutureByBank").send(self, pRspRepeal = pRspRepeal)

    def OnRtnRepealFromBankToFutureByFuture(self, pRspRepeal):
        self.log.debug("OnRtnRepealFromBankToFutureByFuture")
        self.log.debug(pRspRepeal)
        signal("OnRtnRepealFromBankToFutureByFuture").send(self, pRspRepeal = pRspRepeal)

    def OnRtnRepealFromBankToFutureByFutureManual(self, pRspRepeal):
        self.log.debug("OnRtnRepealFromBankToFutureByFutureManual")
        self.log.debug(pRspRepeal)
        signal("OnRtnRepealFromBankToFutureByFutureManual").send(self, pRspRepeal = pRspRepeal)

    def OnRtnRepealFromFutureToBankByBank(self, pRspRepeal):
        self.log.debug("OnRtnRepealFromFutureToBankByBank")
        self.log.debug(pRspRepeal)
        signal("OnRtnRepealFromFutureToBankByBank").send(self, pRspRepeal = pRspRepeal)

    def OnRtnRepealFromFutureToBankByFuture(self, pRspRepeal):
        self.log.debug("OnRtnRepealFromFutureToBankByFuture")
        self.log.debug(pRspRepeal)
        signal("OnRtnRepealFromFutureToBankByFuture").send(self, pRspRepeal = pRspRepeal)

    def OnRtnRepealFromFutureToBankByFutureManual(self, pRspRepeal):
        self.log.debug("OnRtnRepealFromFutureToBankByFutureManual")
        self.log.debug(pRspRepeal)
        signal("OnRtnRepealFromFutureToBankByFutureManual").send(self, pRspRepeal = pRspRepeal)

    def OnRtnTrade(self, pTrade):
        self.log.debug("OnRtnTrade")
        self.log.debug(pTrade)
        signal("OnRtnTrade").send(self, pTrade = pTrade)

    def OnRtnTradingNotice(self, pTradingNoticeInfo):
        self.log.debug("OnRtnTradingNotice")
        self.log.debug(pTradingNoticeInfo)
        signal("OnRtnTradingNotice").send(self, pTradingNoticeInfo = pTradingNoticeInfo)
    def myReqAuthenticate(self, *args, **kwargs):
        self.log.debug("myReqAuthenticate")
        self.requestID += 1
        requestID = self.requestID
        pReqAuthenticate = ApiStruct.ReqAuthenticate(**kwargs)
        pReqAuthenticate.BrokerID = self.BrokerID
        pReqAuthenticate.InvestorID= self.InvestorID
        self.queue.put((1000, lambda :self.ReqAuthenticate(pReqAuthenticate, requestID)))

    def myReqFromBankToFutureByFuture(self, *args, **kwargs):
        self.log.debug("myReqFromBankToFutureByFuture")
        self.requestID += 1
        requestID = self.requestID
        pReqTransfer = ApiStruct.ReqTransfer(**kwargs)
        pReqTransfer.BrokerID = self.BrokerID
        pReqTransfer.InvestorID= self.InvestorID
        self.queue.put((1000, lambda :self.ReqFromBankToFutureByFuture(pReqTransfer, requestID)))

    def myReqFromFutureToBankByFuture(self, *args, **kwargs):
        self.log.debug("myReqFromFutureToBankByFuture")
        self.requestID += 1
        requestID = self.requestID
        pReqTransfer = ApiStruct.ReqTransfer(**kwargs)
        pReqTransfer.BrokerID = self.BrokerID
        pReqTransfer.InvestorID= self.InvestorID
        self.queue.put((1000, lambda :self.ReqFromFutureToBankByFuture(pReqTransfer, requestID)))

    def myReqOrderAction(self, *args, **kwargs):
        self.log.debug("myReqOrderAction")
        self.requestID += 1
        requestID = self.requestID
        pInputOrderAction = ApiStruct.InputOrderAction(**kwargs)
        pInputOrderAction.BrokerID = self.BrokerID
        pInputOrderAction.InvestorID= self.InvestorID
        self.queue.put((1000, lambda :self.ReqOrderAction(pInputOrderAction, requestID)))

    def myReqOrderInsert(self, *args, **kwargs):
        self.log.debug("myReqOrderInsert")
        self.requestID += 1
        requestID = self.requestID
        pInputOrder = ApiStruct.InputOrder(**kwargs)
        pInputOrder.BrokerID = self.BrokerID
        pInputOrder.InvestorID= self.InvestorID
        self.queue.put((1000, lambda :self.ReqOrderInsert(pInputOrder, requestID)))

    def myReqParkedOrderAction(self, *args, **kwargs):
        self.log.debug("myReqParkedOrderAction")
        self.requestID += 1
        requestID = self.requestID
        pParkedOrderAction = ApiStruct.ParkedOrderAction(**kwargs)
        pParkedOrderAction.BrokerID = self.BrokerID
        pParkedOrderAction.InvestorID= self.InvestorID
        self.queue.put((1000, lambda :self.ReqParkedOrderAction(pParkedOrderAction, requestID)))

    def myReqParkedOrderInsert(self, *args, **kwargs):
        self.log.debug("myReqParkedOrderInsert")
        self.requestID += 1
        requestID = self.requestID
        pParkedOrder = ApiStruct.ParkedOrder(**kwargs)
        pParkedOrder.BrokerID = self.BrokerID
        pParkedOrder.InvestorID= self.InvestorID
        self.queue.put((1000, lambda :self.ReqParkedOrderInsert(pParkedOrder, requestID)))

    def myReqQryAccountregister(self, *args, **kwargs):
        self.log.debug("myReqQryAccountregister")
        self.requestID += 1
        requestID = self.requestID
        pQryAccountregister = ApiStruct.QryAccountregister(**kwargs)
        pQryAccountregister.BrokerID = self.BrokerID
        pQryAccountregister.InvestorID= self.InvestorID
        self.queue.put((1000, lambda :self.ReqQryAccountregister(pQryAccountregister, requestID)))

    def myReqQryBrokerTradingAlgos(self, *args, **kwargs):
        self.log.debug("myReqQryBrokerTradingAlgos")
        self.requestID += 1
        requestID = self.requestID
        pQryBrokerTradingAlgos = ApiStruct.QryBrokerTradingAlgos(**kwargs)
        pQryBrokerTradingAlgos.BrokerID = self.BrokerID
        pQryBrokerTradingAlgos.InvestorID= self.InvestorID
        self.queue.put((1000, lambda :self.ReqQryBrokerTradingAlgos(pQryBrokerTradingAlgos, requestID)))

    def myReqQryBrokerTradingParams(self, *args, **kwargs):
        self.log.debug("myReqQryBrokerTradingParams")
        self.requestID += 1
        requestID = self.requestID
        pQryBrokerTradingParams = ApiStruct.QryBrokerTradingParams(**kwargs)
        pQryBrokerTradingParams.BrokerID = self.BrokerID
        pQryBrokerTradingParams.InvestorID= self.InvestorID
        self.queue.put((1000, lambda :self.ReqQryBrokerTradingParams(pQryBrokerTradingParams, requestID)))

    def myReqQryCFMMCTradingAccountKey(self, *args, **kwargs):
        self.log.debug("myReqQryCFMMCTradingAccountKey")
        self.requestID += 1
        requestID = self.requestID
        pQryCFMMCTradingAccountKey = ApiStruct.QryCFMMCTradingAccountKey(**kwargs)
        pQryCFMMCTradingAccountKey.BrokerID = self.BrokerID
        pQryCFMMCTradingAccountKey.InvestorID= self.InvestorID
        self.queue.put((1000, lambda :self.ReqQryCFMMCTradingAccountKey(pQryCFMMCTradingAccountKey, requestID)))

    def myReqQryContractBank(self, *args, **kwargs):
        self.log.debug("myReqQryContractBank")
        self.requestID += 1
        requestID = self.requestID
        pQryContractBank = ApiStruct.QryContractBank(**kwargs)
        pQryContractBank.BrokerID = self.BrokerID
        pQryContractBank.InvestorID= self.InvestorID
        self.queue.put((1000, lambda :self.ReqQryContractBank(pQryContractBank, requestID)))

    def myReqQryDepthMarketData(self, *args, **kwargs):
        self.log.debug("myReqQryDepthMarketData")
        self.requestID += 1
        requestID = self.requestID
        pQryDepthMarketData = ApiStruct.QryDepthMarketData(**kwargs)
        pQryDepthMarketData.BrokerID = self.BrokerID
        pQryDepthMarketData.InvestorID= self.InvestorID
        self.queue.put((1000, lambda :self.ReqQryDepthMarketData(pQryDepthMarketData, requestID)))

    def myReqQryEWarrantOffset(self, *args, **kwargs):
        self.log.debug("myReqQryEWarrantOffset")
        self.requestID += 1
        requestID = self.requestID
        pQryEWarrantOffset = ApiStruct.QryEWarrantOffset(**kwargs)
        pQryEWarrantOffset.BrokerID = self.BrokerID
        pQryEWarrantOffset.InvestorID= self.InvestorID
        self.queue.put((1000, lambda :self.ReqQryEWarrantOffset(pQryEWarrantOffset, requestID)))

    def myReqQryExchange(self, *args, **kwargs):
        self.log.debug("myReqQryExchange")
        self.requestID += 1
        requestID = self.requestID
        pQryExchange = ApiStruct.QryExchange(**kwargs)
        pQryExchange.BrokerID = self.BrokerID
        pQryExchange.InvestorID= self.InvestorID
        self.queue.put((1000, lambda :self.ReqQryExchange(pQryExchange, requestID)))

    def myReqQryExchangeMarginRate(self, *args, **kwargs):
        self.log.debug("myReqQryExchangeMarginRate")
        self.requestID += 1
        requestID = self.requestID
        pQryExchangeMarginRate = ApiStruct.QryExchangeMarginRate(**kwargs)
        pQryExchangeMarginRate.BrokerID = self.BrokerID
        pQryExchangeMarginRate.InvestorID= self.InvestorID
        self.queue.put((1000, lambda :self.ReqQryExchangeMarginRate(pQryExchangeMarginRate, requestID)))

    def myReqQryExchangeMarginRateAdjust(self, *args, **kwargs):
        self.log.debug("myReqQryExchangeMarginRateAdjust")
        self.requestID += 1
        requestID = self.requestID
        pQryExchangeMarginRateAdjust = ApiStruct.QryExchangeMarginRateAdjust(**kwargs)
        pQryExchangeMarginRateAdjust.BrokerID = self.BrokerID
        pQryExchangeMarginRateAdjust.InvestorID= self.InvestorID
        self.queue.put((1000, lambda :self.ReqQryExchangeMarginRateAdjust(pQryExchangeMarginRateAdjust, requestID)))

    def myReqQryExchangeRate(self, *args, **kwargs):
        self.log.debug("myReqQryExchangeRate")
        self.requestID += 1
        requestID = self.requestID
        pQryExchangeRate = ApiStruct.QryExchangeRate(**kwargs)
        pQryExchangeRate.BrokerID = self.BrokerID
        pQryExchangeRate.InvestorID= self.InvestorID
        self.queue.put((1000, lambda :self.ReqQryExchangeRate(pQryExchangeRate, requestID)))

    def myReqQryInstrument(self, *args, **kwargs):
        self.log.debug("myReqQryInstrument")
        self.requestID += 1
        requestID = self.requestID
        pQryInstrument = ApiStruct.QryInstrument(**kwargs)
        pQryInstrument.BrokerID = self.BrokerID
        pQryInstrument.InvestorID= self.InvestorID
        self.queue.put((1000, lambda :self.ReqQryInstrument(pQryInstrument, requestID)))

    def myReqQryInstrumentCommissionRate(self, *args, **kwargs):
        self.log.debug("myReqQryInstrumentCommissionRate")
        self.requestID += 1
        requestID = self.requestID
        pQryInstrumentCommissionRate = ApiStruct.QryInstrumentCommissionRate(**kwargs)
        pQryInstrumentCommissionRate.BrokerID = self.BrokerID
        pQryInstrumentCommissionRate.InvestorID= self.InvestorID
        self.queue.put((1000, lambda :self.ReqQryInstrumentCommissionRate(pQryInstrumentCommissionRate, requestID)))

    def myReqQryInstrumentMarginRate(self, *args, **kwargs):
        self.log.debug("myReqQryInstrumentMarginRate")
        self.requestID += 1
        requestID = self.requestID
        pQryInstrumentMarginRate = ApiStruct.QryInstrumentMarginRate(**kwargs)
        pQryInstrumentMarginRate.BrokerID = self.BrokerID
        pQryInstrumentMarginRate.InvestorID= self.InvestorID
        self.queue.put((1000, lambda :self.ReqQryInstrumentMarginRate(pQryInstrumentMarginRate, requestID)))

    def myReqQryInvestor(self, *args, **kwargs):
        self.log.debug("myReqQryInvestor")
        self.requestID += 1
        requestID = self.requestID
        pQryInvestor = ApiStruct.QryInvestor(**kwargs)
        pQryInvestor.BrokerID = self.BrokerID
        pQryInvestor.InvestorID= self.InvestorID
        self.queue.put((1000, lambda :self.ReqQryInvestor(pQryInvestor, requestID)))

    def myReqQryInvestorPosition(self, *args, **kwargs):
        self.log.debug("myReqQryInvestorPosition")
        self.requestID += 1
        requestID = self.requestID
        pQryInvestorPosition = ApiStruct.QryInvestorPosition(**kwargs)
        pQryInvestorPosition.BrokerID = self.BrokerID
        pQryInvestorPosition.InvestorID= self.InvestorID
        self.queue.put((1000, lambda :self.ReqQryInvestorPosition(pQryInvestorPosition, requestID)))

    def myReqQryInvestorPositionCombineDetail(self, *args, **kwargs):
        self.log.debug("myReqQryInvestorPositionCombineDetail")
        self.requestID += 1
        requestID = self.requestID
        pQryInvestorPositionCombineDetail = ApiStruct.QryInvestorPositionCombineDetail(**kwargs)
        pQryInvestorPositionCombineDetail.BrokerID = self.BrokerID
        pQryInvestorPositionCombineDetail.InvestorID= self.InvestorID
        self.queue.put((1000, lambda :self.ReqQryInvestorPositionCombineDetail(pQryInvestorPositionCombineDetail, requestID)))

    def myReqQryInvestorPositionDetail(self, *args, **kwargs):
        self.log.debug("myReqQryInvestorPositionDetail")
        self.requestID += 1
        requestID = self.requestID
        pQryInvestorPositionDetail = ApiStruct.QryInvestorPositionDetail(**kwargs)
        pQryInvestorPositionDetail.BrokerID = self.BrokerID
        pQryInvestorPositionDetail.InvestorID= self.InvestorID
        self.queue.put((1000, lambda :self.ReqQryInvestorPositionDetail(pQryInvestorPositionDetail, requestID)))

    def myReqQryInvestorProductGroupMargin(self, *args, **kwargs):
        self.log.debug("myReqQryInvestorProductGroupMargin")
        self.requestID += 1
        requestID = self.requestID
        pQryInvestorProductGroupMargin = ApiStruct.QryInvestorProductGroupMargin(**kwargs)
        pQryInvestorProductGroupMargin.BrokerID = self.BrokerID
        pQryInvestorProductGroupMargin.InvestorID= self.InvestorID
        self.queue.put((1000, lambda :self.ReqQryInvestorProductGroupMargin(pQryInvestorProductGroupMargin, requestID)))

    def myReqQryNotice(self, *args, **kwargs):
        self.log.debug("myReqQryNotice")
        self.requestID += 1
        requestID = self.requestID
        pQryNotice = ApiStruct.QryNotice(**kwargs)
        pQryNotice.BrokerID = self.BrokerID
        pQryNotice.InvestorID= self.InvestorID
        self.queue.put((1000, lambda :self.ReqQryNotice(pQryNotice, requestID)))

    def myReqQryOrder(self, *args, **kwargs):
        self.log.debug("myReqQryOrder")
        self.requestID += 1
        requestID = self.requestID
        pQryOrder = ApiStruct.QryOrder(**kwargs)
        pQryOrder.BrokerID = self.BrokerID
        pQryOrder.InvestorID= self.InvestorID
        self.queue.put((1000, lambda :self.ReqQryOrder(pQryOrder, requestID)))

    def myReqQryParkedOrder(self, *args, **kwargs):
        self.log.debug("myReqQryParkedOrder")
        self.requestID += 1
        requestID = self.requestID
        pQryParkedOrder = ApiStruct.QryParkedOrder(**kwargs)
        pQryParkedOrder.BrokerID = self.BrokerID
        pQryParkedOrder.InvestorID= self.InvestorID
        self.queue.put((1000, lambda :self.ReqQryParkedOrder(pQryParkedOrder, requestID)))

    def myReqQryParkedOrderAction(self, *args, **kwargs):
        self.log.debug("myReqQryParkedOrderAction")
        self.requestID += 1
        requestID = self.requestID
        pQryParkedOrderAction = ApiStruct.QryParkedOrderAction(**kwargs)
        pQryParkedOrderAction.BrokerID = self.BrokerID
        pQryParkedOrderAction.InvestorID= self.InvestorID
        self.queue.put((1000, lambda :self.ReqQryParkedOrderAction(pQryParkedOrderAction, requestID)))

    def myReqQryProduct(self, *args, **kwargs):
        self.log.debug("myReqQryProduct")
        self.requestID += 1
        requestID = self.requestID
        pQryProduct = ApiStruct.QryProduct(**kwargs)
        pQryProduct.BrokerID = self.BrokerID
        pQryProduct.InvestorID= self.InvestorID
        self.queue.put((1000, lambda :self.ReqQryProduct(pQryProduct, requestID)))

    def myReqQrySecAgentACIDMap(self, *args, **kwargs):
        self.log.debug("myReqQrySecAgentACIDMap")
        self.requestID += 1
        requestID = self.requestID
        pQrySecAgentACIDMap = ApiStruct.QrySecAgentACIDMap(**kwargs)
        pQrySecAgentACIDMap.BrokerID = self.BrokerID
        pQrySecAgentACIDMap.InvestorID= self.InvestorID
        self.queue.put((1000, lambda :self.ReqQrySecAgentACIDMap(pQrySecAgentACIDMap, requestID)))

    def myReqQrySettlementInfo(self, *args, **kwargs):
        self.log.debug("myReqQrySettlementInfo")
        self.requestID += 1
        requestID = self.requestID
        pQrySettlementInfo = ApiStruct.QrySettlementInfo(**kwargs)
        pQrySettlementInfo.BrokerID = self.BrokerID
        pQrySettlementInfo.InvestorID= self.InvestorID
        self.queue.put((1000, lambda :self.ReqQrySettlementInfo(pQrySettlementInfo, requestID)))

    def myReqQrySettlementInfoConfirm(self, *args, **kwargs):
        self.log.debug("myReqQrySettlementInfoConfirm")
        self.requestID += 1
        requestID = self.requestID
        pQrySettlementInfoConfirm = ApiStruct.QrySettlementInfoConfirm(**kwargs)
        pQrySettlementInfoConfirm.BrokerID = self.BrokerID
        pQrySettlementInfoConfirm.InvestorID= self.InvestorID
        self.queue.put((1000, lambda :self.ReqQrySettlementInfoConfirm(pQrySettlementInfoConfirm, requestID)))

    def myReqQryTrade(self, *args, **kwargs):
        self.log.debug("myReqQryTrade")
        self.requestID += 1
        requestID = self.requestID
        pQryTrade = ApiStruct.QryTrade(**kwargs)
        pQryTrade.BrokerID = self.BrokerID
        pQryTrade.InvestorID= self.InvestorID
        self.queue.put((1000, lambda :self.ReqQryTrade(pQryTrade, requestID)))

    def myReqQryTradingAccount(self, *args, **kwargs):
        self.log.debug("myReqQryTradingAccount")
        self.requestID += 1
        requestID = self.requestID
        pQryTradingAccount = ApiStruct.QryTradingAccount(**kwargs)
        pQryTradingAccount.BrokerID = self.BrokerID
        pQryTradingAccount.InvestorID= self.InvestorID
        self.queue.put((1000, lambda :self.ReqQryTradingAccount(pQryTradingAccount, requestID)))

    def myReqQryTradingCode(self, *args, **kwargs):
        self.log.debug("myReqQryTradingCode")
        self.requestID += 1
        requestID = self.requestID
        pQryTradingCode = ApiStruct.QryTradingCode(**kwargs)
        pQryTradingCode.BrokerID = self.BrokerID
        pQryTradingCode.InvestorID= self.InvestorID
        self.queue.put((1000, lambda :self.ReqQryTradingCode(pQryTradingCode, requestID)))

    def myReqQryTradingNotice(self, *args, **kwargs):
        self.log.debug("myReqQryTradingNotice")
        self.requestID += 1
        requestID = self.requestID
        pQryTradingNotice = ApiStruct.QryTradingNotice(**kwargs)
        pQryTradingNotice.BrokerID = self.BrokerID
        pQryTradingNotice.InvestorID= self.InvestorID
        self.queue.put((1000, lambda :self.ReqQryTradingNotice(pQryTradingNotice, requestID)))

    def myReqQryTransferBank(self, *args, **kwargs):
        self.log.debug("myReqQryTransferBank")
        self.requestID += 1
        requestID = self.requestID
        pQryTransferBank = ApiStruct.QryTransferBank(**kwargs)
        pQryTransferBank.BrokerID = self.BrokerID
        pQryTransferBank.InvestorID= self.InvestorID
        self.queue.put((1000, lambda :self.ReqQryTransferBank(pQryTransferBank, requestID)))

    def myReqQryTransferSerial(self, *args, **kwargs):
        self.log.debug("myReqQryTransferSerial")
        self.requestID += 1
        requestID = self.requestID
        pQryTransferSerial = ApiStruct.QryTransferSerial(**kwargs)
        pQryTransferSerial.BrokerID = self.BrokerID
        pQryTransferSerial.InvestorID= self.InvestorID
        self.queue.put((1000, lambda :self.ReqQryTransferSerial(pQryTransferSerial, requestID)))

    def myReqQueryBankAccountMoneyByFuture(self, *args, **kwargs):
        self.log.debug("myReqQueryBankAccountMoneyByFuture")
        self.requestID += 1
        requestID = self.requestID
        pReqQueryAccount = ApiStruct.ReqQueryAccount(**kwargs)
        pReqQueryAccount.BrokerID = self.BrokerID
        pReqQueryAccount.InvestorID= self.InvestorID
        self.queue.put((1000, lambda :self.ReqQueryBankAccountMoneyByFuture(pReqQueryAccount, requestID)))

    def myReqQueryCFMMCTradingAccountToken(self, *args, **kwargs):
        self.log.debug("myReqQueryCFMMCTradingAccountToken")
        self.requestID += 1
        requestID = self.requestID
        pQueryCFMMCTradingAccountToken = ApiStruct.QueryCFMMCTradingAccountToken(**kwargs)
        pQueryCFMMCTradingAccountToken.BrokerID = self.BrokerID
        pQueryCFMMCTradingAccountToken.InvestorID= self.InvestorID
        self.queue.put((1000, lambda :self.ReqQueryCFMMCTradingAccountToken(pQueryCFMMCTradingAccountToken, requestID)))

    def myReqQueryMaxOrderVolume(self, *args, **kwargs):
        self.log.debug("myReqQueryMaxOrderVolume")
        self.requestID += 1
        requestID = self.requestID
        pQueryMaxOrderVolume = ApiStruct.QueryMaxOrderVolume(**kwargs)
        pQueryMaxOrderVolume.BrokerID = self.BrokerID
        pQueryMaxOrderVolume.InvestorID= self.InvestorID
        self.queue.put((1000, lambda :self.ReqQueryMaxOrderVolume(pQueryMaxOrderVolume, requestID)))

    def myReqRemoveParkedOrder(self, *args, **kwargs):
        self.log.debug("myReqRemoveParkedOrder")
        self.requestID += 1
        requestID = self.requestID
        pRemoveParkedOrder = ApiStruct.RemoveParkedOrder(**kwargs)
        pRemoveParkedOrder.BrokerID = self.BrokerID
        pRemoveParkedOrder.InvestorID= self.InvestorID
        self.queue.put((1000, lambda :self.ReqRemoveParkedOrder(pRemoveParkedOrder, requestID)))

    def myReqRemoveParkedOrderAction(self, *args, **kwargs):
        self.log.debug("myReqRemoveParkedOrderAction")
        self.requestID += 1
        requestID = self.requestID
        pRemoveParkedOrderAction = ApiStruct.RemoveParkedOrderAction(**kwargs)
        pRemoveParkedOrderAction.BrokerID = self.BrokerID
        pRemoveParkedOrderAction.InvestorID= self.InvestorID
        self.queue.put((1000, lambda :self.ReqRemoveParkedOrderAction(pRemoveParkedOrderAction, requestID)))

    def myReqSettlementInfoConfirm(self, *args, **kwargs):
        self.log.debug("myReqSettlementInfoConfirm")
        self.requestID += 1
        requestID = self.requestID
        pSettlementInfoConfirm = ApiStruct.SettlementInfoConfirm(**kwargs)
        pSettlementInfoConfirm.BrokerID = self.BrokerID
        pSettlementInfoConfirm.InvestorID= self.InvestorID
        self.queue.put((1000, lambda :self.ReqSettlementInfoConfirm(pSettlementInfoConfirm, requestID)))

    def myReqTradingAccountPasswordUpdate(self, *args, **kwargs):
        self.log.debug("myReqTradingAccountPasswordUpdate")
        self.requestID += 1
        requestID = self.requestID
        pTradingAccountPasswordUpdate = ApiStruct.TradingAccountPasswordUpdate(**kwargs)
        pTradingAccountPasswordUpdate.BrokerID = self.BrokerID
        pTradingAccountPasswordUpdate.InvestorID= self.InvestorID
        self.queue.put((1000, lambda :self.ReqTradingAccountPasswordUpdate(pTradingAccountPasswordUpdate, requestID)))

    def myReqUserLogin(self, *args, **kwargs):
        self.log.debug("myReqUserLogin")
        self.requestID += 1
        requestID = self.requestID
        pReqUserLogin = ApiStruct.ReqUserLogin(**kwargs)
        pReqUserLogin.BrokerID = self.BrokerID
        pReqUserLogin.InvestorID= self.InvestorID
        self.queue.put((1000, lambda :self.ReqUserLogin(pReqUserLogin, requestID)))

    def myReqUserLogout(self, *args, **kwargs):
        self.log.debug("myReqUserLogout")
        self.requestID += 1
        requestID = self.requestID
        pUserLogout = ApiStruct.UserLogout(**kwargs)
        pUserLogout.BrokerID = self.BrokerID
        pUserLogout.InvestorID= self.InvestorID
        self.queue.put((1000, lambda :self.ReqUserLogout(pUserLogout, requestID)))

    def myReqUserPasswordUpdate(self, *args, **kwargs):
        self.log.debug("myReqUserPasswordUpdate")
        self.requestID += 1
        requestID = self.requestID
        pUserPasswordUpdate = ApiStruct.UserPasswordUpdate(**kwargs)
        pUserPasswordUpdate.BrokerID = self.BrokerID
        pUserPasswordUpdate.InvestorID= self.InvestorID
        self.queue.put((1000, lambda :self.ReqUserPasswordUpdate(pUserPasswordUpdate, requestID)))

