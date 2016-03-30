import logging
from ctp.futures import TraderApi,ApiStruct
from blinker import signal
class MyTraderApi(TraderApi):
    def __init__(self):
        self.log = logging.getLogger("MyTraderApi")
        self.requestID = 1
        self.BrokerID = "8000"
        self.InvestorID = "81180429"

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
        pReqAuthenticate = ApiStruct.ReqAuthenticate(**kwargs)
        pReqAuthenticate.BrokerID = self.BrokerID
        pReqAuthenticate.InvestorID= self.InvestorID
        self.ReqAuthenticate(pReqAuthenticate, self.requestID)

    def myReqFromBankToFutureByFuture(self, *args, **kwargs):
        self.log.debug("myReqFromBankToFutureByFuture")
        self.requestID += 1
        pReqTransfer = ApiStruct.ReqTransfer(**kwargs)
        pReqTransfer.BrokerID = self.BrokerID
        pReqTransfer.InvestorID= self.InvestorID
        self.ReqFromBankToFutureByFuture(pReqTransfer, self.requestID)

    def myReqFromFutureToBankByFuture(self, *args, **kwargs):
        self.log.debug("myReqFromFutureToBankByFuture")
        self.requestID += 1
        pReqTransfer = ApiStruct.ReqTransfer(**kwargs)
        pReqTransfer.BrokerID = self.BrokerID
        pReqTransfer.InvestorID= self.InvestorID
        self.ReqFromFutureToBankByFuture(pReqTransfer, self.requestID)

    def myReqOrderAction(self, *args, **kwargs):
        self.log.debug("myReqOrderAction")
        self.requestID += 1
        pInputOrderAction = ApiStruct.InputOrderAction(**kwargs)
        pInputOrderAction.BrokerID = self.BrokerID
        pInputOrderAction.InvestorID= self.InvestorID
        self.ReqOrderAction(pInputOrderAction, self.requestID)

    def myReqOrderInsert(self, *args, **kwargs):
        self.log.debug("myReqOrderInsert")
        self.requestID += 1
        pInputOrder = ApiStruct.InputOrder(**kwargs)
        pInputOrder.BrokerID = self.BrokerID
        pInputOrder.InvestorID= self.InvestorID
        self.ReqOrderInsert(pInputOrder, self.requestID)

    def myReqParkedOrderAction(self, *args, **kwargs):
        self.log.debug("myReqParkedOrderAction")
        self.requestID += 1
        pParkedOrderAction = ApiStruct.ParkedOrderAction(**kwargs)
        pParkedOrderAction.BrokerID = self.BrokerID
        pParkedOrderAction.InvestorID= self.InvestorID
        self.ReqParkedOrderAction(pParkedOrderAction, self.requestID)

    def myReqParkedOrderInsert(self, *args, **kwargs):
        self.log.debug("myReqParkedOrderInsert")
        self.requestID += 1
        pParkedOrder = ApiStruct.ParkedOrder(**kwargs)
        pParkedOrder.BrokerID = self.BrokerID
        pParkedOrder.InvestorID= self.InvestorID
        self.ReqParkedOrderInsert(pParkedOrder, self.requestID)

    def myReqQryAccountregister(self, *args, **kwargs):
        self.log.debug("myReqQryAccountregister")
        self.requestID += 1
        pQryAccountregister = ApiStruct.QryAccountregister(**kwargs)
        pQryAccountregister.BrokerID = self.BrokerID
        pQryAccountregister.InvestorID= self.InvestorID
        self.ReqQryAccountregister(pQryAccountregister, self.requestID)

    def myReqQryBrokerTradingAlgos(self, *args, **kwargs):
        self.log.debug("myReqQryBrokerTradingAlgos")
        self.requestID += 1
        pQryBrokerTradingAlgos = ApiStruct.QryBrokerTradingAlgos(**kwargs)
        pQryBrokerTradingAlgos.BrokerID = self.BrokerID
        pQryBrokerTradingAlgos.InvestorID= self.InvestorID
        self.ReqQryBrokerTradingAlgos(pQryBrokerTradingAlgos, self.requestID)

    def myReqQryBrokerTradingParams(self, *args, **kwargs):
        self.log.debug("myReqQryBrokerTradingParams")
        self.requestID += 1
        pQryBrokerTradingParams = ApiStruct.QryBrokerTradingParams(**kwargs)
        pQryBrokerTradingParams.BrokerID = self.BrokerID
        pQryBrokerTradingParams.InvestorID= self.InvestorID
        self.ReqQryBrokerTradingParams(pQryBrokerTradingParams, self.requestID)

    def myReqQryCFMMCTradingAccountKey(self, *args, **kwargs):
        self.log.debug("myReqQryCFMMCTradingAccountKey")
        self.requestID += 1
        pQryCFMMCTradingAccountKey = ApiStruct.QryCFMMCTradingAccountKey(**kwargs)
        pQryCFMMCTradingAccountKey.BrokerID = self.BrokerID
        pQryCFMMCTradingAccountKey.InvestorID= self.InvestorID
        self.ReqQryCFMMCTradingAccountKey(pQryCFMMCTradingAccountKey, self.requestID)

    def myReqQryContractBank(self, *args, **kwargs):
        self.log.debug("myReqQryContractBank")
        self.requestID += 1
        pQryContractBank = ApiStruct.QryContractBank(**kwargs)
        pQryContractBank.BrokerID = self.BrokerID
        pQryContractBank.InvestorID= self.InvestorID
        self.ReqQryContractBank(pQryContractBank, self.requestID)

    def myReqQryDepthMarketData(self, *args, **kwargs):
        self.log.debug("myReqQryDepthMarketData")
        self.requestID += 1
        pQryDepthMarketData = ApiStruct.QryDepthMarketData(**kwargs)
        pQryDepthMarketData.BrokerID = self.BrokerID
        pQryDepthMarketData.InvestorID= self.InvestorID
        self.ReqQryDepthMarketData(pQryDepthMarketData, self.requestID)

    def myReqQryEWarrantOffset(self, *args, **kwargs):
        self.log.debug("myReqQryEWarrantOffset")
        self.requestID += 1
        pQryEWarrantOffset = ApiStruct.QryEWarrantOffset(**kwargs)
        pQryEWarrantOffset.BrokerID = self.BrokerID
        pQryEWarrantOffset.InvestorID= self.InvestorID
        self.ReqQryEWarrantOffset(pQryEWarrantOffset, self.requestID)

    def myReqQryExchange(self, *args, **kwargs):
        self.log.debug("myReqQryExchange")
        self.requestID += 1
        pQryExchange = ApiStruct.QryExchange(**kwargs)
        pQryExchange.BrokerID = self.BrokerID
        pQryExchange.InvestorID= self.InvestorID
        self.ReqQryExchange(pQryExchange, self.requestID)

    def myReqQryExchangeMarginRate(self, *args, **kwargs):
        self.log.debug("myReqQryExchangeMarginRate")
        self.requestID += 1
        pQryExchangeMarginRate = ApiStruct.QryExchangeMarginRate(**kwargs)
        pQryExchangeMarginRate.BrokerID = self.BrokerID
        pQryExchangeMarginRate.InvestorID= self.InvestorID
        self.ReqQryExchangeMarginRate(pQryExchangeMarginRate, self.requestID)

    def myReqQryExchangeMarginRateAdjust(self, *args, **kwargs):
        self.log.debug("myReqQryExchangeMarginRateAdjust")
        self.requestID += 1
        pQryExchangeMarginRateAdjust = ApiStruct.QryExchangeMarginRateAdjust(**kwargs)
        pQryExchangeMarginRateAdjust.BrokerID = self.BrokerID
        pQryExchangeMarginRateAdjust.InvestorID= self.InvestorID
        self.ReqQryExchangeMarginRateAdjust(pQryExchangeMarginRateAdjust, self.requestID)

    def myReqQryExchangeRate(self, *args, **kwargs):
        self.log.debug("myReqQryExchangeRate")
        self.requestID += 1
        pQryExchangeRate = ApiStruct.QryExchangeRate(**kwargs)
        pQryExchangeRate.BrokerID = self.BrokerID
        pQryExchangeRate.InvestorID= self.InvestorID
        self.ReqQryExchangeRate(pQryExchangeRate, self.requestID)

    def myReqQryInstrument(self, *args, **kwargs):
        self.log.debug("myReqQryInstrument")
        self.requestID += 1
        pQryInstrument = ApiStruct.QryInstrument(**kwargs)
        pQryInstrument.BrokerID = self.BrokerID
        pQryInstrument.InvestorID= self.InvestorID
        self.ReqQryInstrument(pQryInstrument, self.requestID)

    def myReqQryInstrumentCommissionRate(self, *args, **kwargs):
        self.log.debug("myReqQryInstrumentCommissionRate")
        self.requestID += 1
        pQryInstrumentCommissionRate = ApiStruct.QryInstrumentCommissionRate(**kwargs)
        pQryInstrumentCommissionRate.BrokerID = self.BrokerID
        pQryInstrumentCommissionRate.InvestorID= self.InvestorID
        self.ReqQryInstrumentCommissionRate(pQryInstrumentCommissionRate, self.requestID)

    def myReqQryInstrumentMarginRate(self, *args, **kwargs):
        self.log.debug("myReqQryInstrumentMarginRate")
        self.requestID += 1
        pQryInstrumentMarginRate = ApiStruct.QryInstrumentMarginRate(**kwargs)
        pQryInstrumentMarginRate.BrokerID = self.BrokerID
        pQryInstrumentMarginRate.InvestorID= self.InvestorID
        self.ReqQryInstrumentMarginRate(pQryInstrumentMarginRate, self.requestID)

    def myReqQryInvestor(self, *args, **kwargs):
        self.log.debug("myReqQryInvestor")
        self.requestID += 1
        pQryInvestor = ApiStruct.QryInvestor(**kwargs)
        pQryInvestor.BrokerID = self.BrokerID
        pQryInvestor.InvestorID= self.InvestorID
        self.ReqQryInvestor(pQryInvestor, self.requestID)

    def myReqQryInvestorPosition(self, *args, **kwargs):
        self.log.debug("myReqQryInvestorPosition")
        self.requestID += 1
        pQryInvestorPosition = ApiStruct.QryInvestorPosition(**kwargs)
        pQryInvestorPosition.BrokerID = self.BrokerID
        pQryInvestorPosition.InvestorID= self.InvestorID
        self.ReqQryInvestorPosition(pQryInvestorPosition, self.requestID)

    def myReqQryInvestorPositionCombineDetail(self, *args, **kwargs):
        self.log.debug("myReqQryInvestorPositionCombineDetail")
        self.requestID += 1
        pQryInvestorPositionCombineDetail = ApiStruct.QryInvestorPositionCombineDetail(**kwargs)
        pQryInvestorPositionCombineDetail.BrokerID = self.BrokerID
        pQryInvestorPositionCombineDetail.InvestorID= self.InvestorID
        self.ReqQryInvestorPositionCombineDetail(pQryInvestorPositionCombineDetail, self.requestID)

    def myReqQryInvestorPositionDetail(self, *args, **kwargs):
        self.log.debug("myReqQryInvestorPositionDetail")
        self.requestID += 1
        pQryInvestorPositionDetail = ApiStruct.QryInvestorPositionDetail(**kwargs)
        pQryInvestorPositionDetail.BrokerID = self.BrokerID
        pQryInvestorPositionDetail.InvestorID= self.InvestorID
        self.ReqQryInvestorPositionDetail(pQryInvestorPositionDetail, self.requestID)

    def myReqQryInvestorProductGroupMargin(self, *args, **kwargs):
        self.log.debug("myReqQryInvestorProductGroupMargin")
        self.requestID += 1
        pQryInvestorProductGroupMargin = ApiStruct.QryInvestorProductGroupMargin(**kwargs)
        pQryInvestorProductGroupMargin.BrokerID = self.BrokerID
        pQryInvestorProductGroupMargin.InvestorID= self.InvestorID
        self.ReqQryInvestorProductGroupMargin(pQryInvestorProductGroupMargin, self.requestID)

    def myReqQryNotice(self, *args, **kwargs):
        self.log.debug("myReqQryNotice")
        self.requestID += 1
        pQryNotice = ApiStruct.QryNotice(**kwargs)
        pQryNotice.BrokerID = self.BrokerID
        pQryNotice.InvestorID= self.InvestorID
        self.ReqQryNotice(pQryNotice, self.requestID)

    def myReqQryOrder(self, *args, **kwargs):
        self.log.debug("myReqQryOrder")
        self.requestID += 1
        pQryOrder = ApiStruct.QryOrder(**kwargs)
        pQryOrder.BrokerID = self.BrokerID
        pQryOrder.InvestorID= self.InvestorID
        self.ReqQryOrder(pQryOrder, self.requestID)

    def myReqQryParkedOrder(self, *args, **kwargs):
        self.log.debug("myReqQryParkedOrder")
        self.requestID += 1
        pQryParkedOrder = ApiStruct.QryParkedOrder(**kwargs)
        pQryParkedOrder.BrokerID = self.BrokerID
        pQryParkedOrder.InvestorID= self.InvestorID
        self.ReqQryParkedOrder(pQryParkedOrder, self.requestID)

    def myReqQryParkedOrderAction(self, *args, **kwargs):
        self.log.debug("myReqQryParkedOrderAction")
        self.requestID += 1
        pQryParkedOrderAction = ApiStruct.QryParkedOrderAction(**kwargs)
        pQryParkedOrderAction.BrokerID = self.BrokerID
        pQryParkedOrderAction.InvestorID= self.InvestorID
        self.ReqQryParkedOrderAction(pQryParkedOrderAction, self.requestID)

    def myReqQryProduct(self, *args, **kwargs):
        self.log.debug("myReqQryProduct")
        self.requestID += 1
        pQryProduct = ApiStruct.QryProduct(**kwargs)
        pQryProduct.BrokerID = self.BrokerID
        pQryProduct.InvestorID= self.InvestorID
        self.ReqQryProduct(pQryProduct, self.requestID)

    def myReqQrySecAgentACIDMap(self, *args, **kwargs):
        self.log.debug("myReqQrySecAgentACIDMap")
        self.requestID += 1
        pQrySecAgentACIDMap = ApiStruct.QrySecAgentACIDMap(**kwargs)
        pQrySecAgentACIDMap.BrokerID = self.BrokerID
        pQrySecAgentACIDMap.InvestorID= self.InvestorID
        self.ReqQrySecAgentACIDMap(pQrySecAgentACIDMap, self.requestID)

    def myReqQrySettlementInfo(self, *args, **kwargs):
        self.log.debug("myReqQrySettlementInfo")
        self.requestID += 1
        pQrySettlementInfo = ApiStruct.QrySettlementInfo(**kwargs)
        pQrySettlementInfo.BrokerID = self.BrokerID
        pQrySettlementInfo.InvestorID= self.InvestorID
        self.ReqQrySettlementInfo(pQrySettlementInfo, self.requestID)

    def myReqQrySettlementInfoConfirm(self, *args, **kwargs):
        self.log.debug("myReqQrySettlementInfoConfirm")
        self.requestID += 1
        pQrySettlementInfoConfirm = ApiStruct.QrySettlementInfoConfirm(**kwargs)
        pQrySettlementInfoConfirm.BrokerID = self.BrokerID
        pQrySettlementInfoConfirm.InvestorID= self.InvestorID
        self.ReqQrySettlementInfoConfirm(pQrySettlementInfoConfirm, self.requestID)

    def myReqQryTrade(self, *args, **kwargs):
        self.log.debug("myReqQryTrade")
        self.requestID += 1
        pQryTrade = ApiStruct.QryTrade(**kwargs)
        pQryTrade.BrokerID = self.BrokerID
        pQryTrade.InvestorID= self.InvestorID
        self.ReqQryTrade(pQryTrade, self.requestID)

    def myReqQryTradingAccount(self, *args, **kwargs):
        self.log.debug("myReqQryTradingAccount")
        self.requestID += 1
        pQryTradingAccount = ApiStruct.QryTradingAccount(**kwargs)
        pQryTradingAccount.BrokerID = self.BrokerID
        pQryTradingAccount.InvestorID= self.InvestorID
        self.ReqQryTradingAccount(pQryTradingAccount, self.requestID)

    def myReqQryTradingCode(self, *args, **kwargs):
        self.log.debug("myReqQryTradingCode")
        self.requestID += 1
        pQryTradingCode = ApiStruct.QryTradingCode(**kwargs)
        pQryTradingCode.BrokerID = self.BrokerID
        pQryTradingCode.InvestorID= self.InvestorID
        self.ReqQryTradingCode(pQryTradingCode, self.requestID)

    def myReqQryTradingNotice(self, *args, **kwargs):
        self.log.debug("myReqQryTradingNotice")
        self.requestID += 1
        pQryTradingNotice = ApiStruct.QryTradingNotice(**kwargs)
        pQryTradingNotice.BrokerID = self.BrokerID
        pQryTradingNotice.InvestorID= self.InvestorID
        self.ReqQryTradingNotice(pQryTradingNotice, self.requestID)

    def myReqQryTransferBank(self, *args, **kwargs):
        self.log.debug("myReqQryTransferBank")
        self.requestID += 1
        pQryTransferBank = ApiStruct.QryTransferBank(**kwargs)
        pQryTransferBank.BrokerID = self.BrokerID
        pQryTransferBank.InvestorID= self.InvestorID
        self.ReqQryTransferBank(pQryTransferBank, self.requestID)

    def myReqQryTransferSerial(self, *args, **kwargs):
        self.log.debug("myReqQryTransferSerial")
        self.requestID += 1
        pQryTransferSerial = ApiStruct.QryTransferSerial(**kwargs)
        pQryTransferSerial.BrokerID = self.BrokerID
        pQryTransferSerial.InvestorID= self.InvestorID
        self.ReqQryTransferSerial(pQryTransferSerial, self.requestID)

    def myReqQueryBankAccountMoneyByFuture(self, *args, **kwargs):
        self.log.debug("myReqQueryBankAccountMoneyByFuture")
        self.requestID += 1
        pReqQueryAccount = ApiStruct.ReqQueryAccount(**kwargs)
        pReqQueryAccount.BrokerID = self.BrokerID
        pReqQueryAccount.InvestorID= self.InvestorID
        self.ReqQueryBankAccountMoneyByFuture(pReqQueryAccount, self.requestID)

    def myReqQueryCFMMCTradingAccountToken(self, *args, **kwargs):
        self.log.debug("myReqQueryCFMMCTradingAccountToken")
        self.requestID += 1
        pQueryCFMMCTradingAccountToken = ApiStruct.QueryCFMMCTradingAccountToken(**kwargs)
        pQueryCFMMCTradingAccountToken.BrokerID = self.BrokerID
        pQueryCFMMCTradingAccountToken.InvestorID= self.InvestorID
        self.ReqQueryCFMMCTradingAccountToken(pQueryCFMMCTradingAccountToken, self.requestID)

    def myReqQueryMaxOrderVolume(self, *args, **kwargs):
        self.log.debug("myReqQueryMaxOrderVolume")
        self.requestID += 1
        pQueryMaxOrderVolume = ApiStruct.QueryMaxOrderVolume(**kwargs)
        pQueryMaxOrderVolume.BrokerID = self.BrokerID
        pQueryMaxOrderVolume.InvestorID= self.InvestorID
        self.ReqQueryMaxOrderVolume(pQueryMaxOrderVolume, self.requestID)

    def myReqRemoveParkedOrder(self, *args, **kwargs):
        self.log.debug("myReqRemoveParkedOrder")
        self.requestID += 1
        pRemoveParkedOrder = ApiStruct.RemoveParkedOrder(**kwargs)
        pRemoveParkedOrder.BrokerID = self.BrokerID
        pRemoveParkedOrder.InvestorID= self.InvestorID
        self.ReqRemoveParkedOrder(pRemoveParkedOrder, self.requestID)

    def myReqRemoveParkedOrderAction(self, *args, **kwargs):
        self.log.debug("myReqRemoveParkedOrderAction")
        self.requestID += 1
        pRemoveParkedOrderAction = ApiStruct.RemoveParkedOrderAction(**kwargs)
        pRemoveParkedOrderAction.BrokerID = self.BrokerID
        pRemoveParkedOrderAction.InvestorID= self.InvestorID
        self.ReqRemoveParkedOrderAction(pRemoveParkedOrderAction, self.requestID)

    def myReqSettlementInfoConfirm(self, *args, **kwargs):
        self.log.debug("myReqSettlementInfoConfirm")
        self.requestID += 1
        pSettlementInfoConfirm = ApiStruct.SettlementInfoConfirm(**kwargs)
        pSettlementInfoConfirm.BrokerID = self.BrokerID
        pSettlementInfoConfirm.InvestorID= self.InvestorID
        self.ReqSettlementInfoConfirm(pSettlementInfoConfirm, self.requestID)

    def myReqTradingAccountPasswordUpdate(self, *args, **kwargs):
        self.log.debug("myReqTradingAccountPasswordUpdate")
        self.requestID += 1
        pTradingAccountPasswordUpdate = ApiStruct.TradingAccountPasswordUpdate(**kwargs)
        pTradingAccountPasswordUpdate.BrokerID = self.BrokerID
        pTradingAccountPasswordUpdate.InvestorID= self.InvestorID
        self.ReqTradingAccountPasswordUpdate(pTradingAccountPasswordUpdate, self.requestID)

    def myReqUserLogin(self, *args, **kwargs):
        self.log.debug("myReqUserLogin")
        self.requestID += 1
        pReqUserLogin = ApiStruct.ReqUserLogin(**kwargs)
        pReqUserLogin.BrokerID = self.BrokerID
        pReqUserLogin.InvestorID= self.InvestorID
        self.ReqUserLogin(pReqUserLogin, self.requestID)

    def myReqUserLogout(self, *args, **kwargs):
        self.log.debug("myReqUserLogout")
        self.requestID += 1
        pUserLogout = ApiStruct.UserLogout(**kwargs)
        pUserLogout.BrokerID = self.BrokerID
        pUserLogout.InvestorID= self.InvestorID
        self.ReqUserLogout(pUserLogout, self.requestID)

    def myReqUserPasswordUpdate(self, *args, **kwargs):
        self.log.debug("myReqUserPasswordUpdate")
        self.requestID += 1
        pUserPasswordUpdate = ApiStruct.UserPasswordUpdate(**kwargs)
        pUserPasswordUpdate.BrokerID = self.BrokerID
        pUserPasswordUpdate.InvestorID= self.InvestorID
        self.ReqUserPasswordUpdate(pUserPasswordUpdate, self.requestID)

