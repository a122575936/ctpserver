import logging
class MyTraderApi(TraderApi):
    def __init__(self):
        self.log = logging.getlogger("MyTraderApi")

    def OnErrRtnBankToFutureByFuture(self, pReqTransfer, pRspInfo):
        log.debug("OnErrRtnBankToFutureByFuture", pReqTransfer, pRspInfo)

    def OnErrRtnFutureToBankByFuture(self, pReqTransfer, pRspInfo):
        log.debug("OnErrRtnFutureToBankByFuture", pReqTransfer, pRspInfo)

    def OnErrRtnOrderAction(self, pOrderAction, pRspInfo):
        log.debug("OnErrRtnOrderAction", pOrderAction, pRspInfo)

    def OnErrRtnOrderInsert(self, pInputOrder, pRspInfo):
        log.debug("OnErrRtnOrderInsert", pInputOrder, pRspInfo)

    def OnErrRtnQueryBankBalanceByFuture(self, pReqQueryAccount, pRspInfo):
        log.debug("OnErrRtnQueryBankBalanceByFuture", pReqQueryAccount, pRspInfo)

    def OnErrRtnRepealBankToFutureByFutureManual(self, pReqRepeal, pRspInfo):
        log.debug("OnErrRtnRepealBankToFutureByFutureManual", pReqRepeal, pRspInfo)

    def OnErrRtnRepealFutureToBankByFutureManual(self, pReqRepeal, pRspInfo):
        log.debug("OnErrRtnRepealFutureToBankByFutureManual", pReqRepeal, pRspInfo)

    def OnFrontConnected(self):
        log.debug("OnFrontConnected", )

    def OnFrontDisconnected(self, nReason):
        log.debug("OnFrontDisconnected", nReason)

    def OnHeartBeatWarning(self, nTimeLapse):
        log.debug("OnHeartBeatWarning", nTimeLapse)

    def OnRspAuthenticate(self, pRspAuthenticate, pRspInfo, nRequestID, bIsLast):
        log.debug("OnRspAuthenticate", pRspAuthenticate, pRspInfo, nRequestID, bIsLast)

    def OnRspError(self, pRspInfo, nRequestID, bIsLast):
        log.debug("OnRspError", pRspInfo, nRequestID, bIsLast)

    def OnRspFromBankToFutureByFuture(self, pReqTransfer, pRspInfo, nRequestID, bIsLast):
        log.debug("OnRspFromBankToFutureByFuture", pReqTransfer, pRspInfo, nRequestID, bIsLast)

    def OnRspFromFutureToBankByFuture(self, pReqTransfer, pRspInfo, nRequestID, bIsLast):
        log.debug("OnRspFromFutureToBankByFuture", pReqTransfer, pRspInfo, nRequestID, bIsLast)

    def OnRspOrderAction(self, pInputOrderAction, pRspInfo, nRequestID, bIsLast):
        log.debug("OnRspOrderAction", pInputOrderAction, pRspInfo, nRequestID, bIsLast)

    def OnRspOrderInsert(self, pInputOrder, pRspInfo, nRequestID, bIsLast):
        log.debug("OnRspOrderInsert", pInputOrder, pRspInfo, nRequestID, bIsLast)

    def OnRspParkedOrderAction(self, pParkedOrderAction, pRspInfo, nRequestID, bIsLast):
        log.debug("OnRspParkedOrderAction", pParkedOrderAction, pRspInfo, nRequestID, bIsLast)

    def OnRspParkedOrderInsert(self, pParkedOrder, pRspInfo, nRequestID, bIsLast):
        log.debug("OnRspParkedOrderInsert", pParkedOrder, pRspInfo, nRequestID, bIsLast)

    def OnRspQryAccountregister(self, pAccountregister, pRspInfo, nRequestID, bIsLast):
        log.debug("OnRspQryAccountregister", pAccountregister, pRspInfo, nRequestID, bIsLast)

    def OnRspQryBrokerTradingAlgos(self, pBrokerTradingAlgos, pRspInfo, nRequestID, bIsLast):
        log.debug("OnRspQryBrokerTradingAlgos", pBrokerTradingAlgos, pRspInfo, nRequestID, bIsLast)

    def OnRspQryBrokerTradingParams(self, pBrokerTradingParams, pRspInfo, nRequestID, bIsLast):
        log.debug("OnRspQryBrokerTradingParams", pBrokerTradingParams, pRspInfo, nRequestID, bIsLast)

    def OnRspQryCFMMCTradingAccountKey(self, pCFMMCTradingAccountKey, pRspInfo, nRequestID, bIsLast):
        log.debug("OnRspQryCFMMCTradingAccountKey", pCFMMCTradingAccountKey, pRspInfo, nRequestID, bIsLast)

    def OnRspQryContractBank(self, pContractBank, pRspInfo, nRequestID, bIsLast):
        log.debug("OnRspQryContractBank", pContractBank, pRspInfo, nRequestID, bIsLast)

    def OnRspQryDepthMarketData(self, pDepthMarketData, pRspInfo, nRequestID, bIsLast):
        log.debug("OnRspQryDepthMarketData", pDepthMarketData, pRspInfo, nRequestID, bIsLast)

    def OnRspQryEWarrantOffset(self, pEWarrantOffset, pRspInfo, nRequestID, bIsLast):
        log.debug("OnRspQryEWarrantOffset", pEWarrantOffset, pRspInfo, nRequestID, bIsLast)

    def OnRspQryExchange(self, pExchange, pRspInfo, nRequestID, bIsLast):
        log.debug("OnRspQryExchange", pExchange, pRspInfo, nRequestID, bIsLast)

    def OnRspQryExchangeMarginRate(self, pExchangeMarginRate, pRspInfo, nRequestID, bIsLast):
        log.debug("OnRspQryExchangeMarginRate", pExchangeMarginRate, pRspInfo, nRequestID, bIsLast)

    def OnRspQryExchangeMarginRateAdjust(self, pExchangeMarginRateAdjust, pRspInfo, nRequestID, bIsLast):
        log.debug("OnRspQryExchangeMarginRateAdjust", pExchangeMarginRateAdjust, pRspInfo, nRequestID, bIsLast)

    def OnRspQryExchangeRate(self, pExchangeRate, pRspInfo, nRequestID, bIsLast):
        log.debug("OnRspQryExchangeRate", pExchangeRate, pRspInfo, nRequestID, bIsLast)

    def OnRspQryInstrument(self, pInstrument, pRspInfo, nRequestID, bIsLast):
        log.debug("OnRspQryInstrument", pInstrument, pRspInfo, nRequestID, bIsLast)

    def OnRspQryInstrumentCommissionRate(self, pInstrumentCommissionRate, pRspInfo, nRequestID, bIsLast):
        log.debug("OnRspQryInstrumentCommissionRate", pInstrumentCommissionRate, pRspInfo, nRequestID, bIsLast)

    def OnRspQryInstrumentMarginRate(self, pInstrumentMarginRate, pRspInfo, nRequestID, bIsLast):
        log.debug("OnRspQryInstrumentMarginRate", pInstrumentMarginRate, pRspInfo, nRequestID, bIsLast)

    def OnRspQryInvestor(self, pInvestor, pRspInfo, nRequestID, bIsLast):
        log.debug("OnRspQryInvestor", pInvestor, pRspInfo, nRequestID, bIsLast)

    def OnRspQryInvestorPosition(self, pInvestorPosition, pRspInfo, nRequestID, bIsLast):
        log.debug("OnRspQryInvestorPosition", pInvestorPosition, pRspInfo, nRequestID, bIsLast)

    def OnRspQryInvestorPositionCombineDetail(self, pInvestorPositionCombineDetail, pRspInfo, nRequestID, bIsLast):
        log.debug("OnRspQryInvestorPositionCombineDetail", pInvestorPositionCombineDetail, pRspInfo, nRequestID, bIsLast)

    def OnRspQryInvestorPositionDetail(self, pInvestorPositionDetail, pRspInfo, nRequestID, bIsLast):
        log.debug("OnRspQryInvestorPositionDetail", pInvestorPositionDetail, pRspInfo, nRequestID, bIsLast)

    def OnRspQryInvestorProductGroupMargin(self, pInvestorProductGroupMargin, pRspInfo, nRequestID, bIsLast):
        log.debug("OnRspQryInvestorProductGroupMargin", pInvestorProductGroupMargin, pRspInfo, nRequestID, bIsLast)

    def OnRspQryNotice(self, pNotice, pRspInfo, nRequestID, bIsLast):
        log.debug("OnRspQryNotice", pNotice, pRspInfo, nRequestID, bIsLast)

    def OnRspQryOrder(self, pOrder, pRspInfo, nRequestID, bIsLast):
        log.debug("OnRspQryOrder", pOrder, pRspInfo, nRequestID, bIsLast)

    def OnRspQryParkedOrder(self, pParkedOrder, pRspInfo, nRequestID, bIsLast):
        log.debug("OnRspQryParkedOrder", pParkedOrder, pRspInfo, nRequestID, bIsLast)

    def OnRspQryParkedOrderAction(self, pParkedOrderAction, pRspInfo, nRequestID, bIsLast):
        log.debug("OnRspQryParkedOrderAction", pParkedOrderAction, pRspInfo, nRequestID, bIsLast)

    def OnRspQryProduct(self, pProduct, pRspInfo, nRequestID, bIsLast):
        log.debug("OnRspQryProduct", pProduct, pRspInfo, nRequestID, bIsLast)

    def OnRspQrySecAgentACIDMap(self, pSecAgentACIDMap, pRspInfo, nRequestID, bIsLast):
        log.debug("OnRspQrySecAgentACIDMap", pSecAgentACIDMap, pRspInfo, nRequestID, bIsLast)

    def OnRspQrySettlementInfo(self, pSettlementInfo, pRspInfo, nRequestID, bIsLast):
        log.debug("OnRspQrySettlementInfo", pSettlementInfo, pRspInfo, nRequestID, bIsLast)

    def OnRspQrySettlementInfoConfirm(self, pSettlementInfoConfirm, pRspInfo, nRequestID, bIsLast):
        log.debug("OnRspQrySettlementInfoConfirm", pSettlementInfoConfirm, pRspInfo, nRequestID, bIsLast)

    def OnRspQryTrade(self, pTrade, pRspInfo, nRequestID, bIsLast):
        log.debug("OnRspQryTrade", pTrade, pRspInfo, nRequestID, bIsLast)

    def OnRspQryTradingAccount(self, pTradingAccount, pRspInfo, nRequestID, bIsLast):
        log.debug("OnRspQryTradingAccount", pTradingAccount, pRspInfo, nRequestID, bIsLast)

    def OnRspQryTradingCode(self, pTradingCode, pRspInfo, nRequestID, bIsLast):
        log.debug("OnRspQryTradingCode", pTradingCode, pRspInfo, nRequestID, bIsLast)

    def OnRspQryTradingNotice(self, pTradingNotice, pRspInfo, nRequestID, bIsLast):
        log.debug("OnRspQryTradingNotice", pTradingNotice, pRspInfo, nRequestID, bIsLast)

    def OnRspQryTransferBank(self, pTransferBank, pRspInfo, nRequestID, bIsLast):
        log.debug("OnRspQryTransferBank", pTransferBank, pRspInfo, nRequestID, bIsLast)

    def OnRspQryTransferSerial(self, pTransferSerial, pRspInfo, nRequestID, bIsLast):
        log.debug("OnRspQryTransferSerial", pTransferSerial, pRspInfo, nRequestID, bIsLast)

    def OnRspQueryBankAccountMoneyByFuture(self, pReqQueryAccount, pRspInfo, nRequestID, bIsLast):
        log.debug("OnRspQueryBankAccountMoneyByFuture", pReqQueryAccount, pRspInfo, nRequestID, bIsLast)

    def OnRspQueryCFMMCTradingAccountToken(self, pQueryCFMMCTradingAccountToken, pRspInfo, nRequestID, bIsLast):
        log.debug("OnRspQueryCFMMCTradingAccountToken", pQueryCFMMCTradingAccountToken, pRspInfo, nRequestID, bIsLast)

    def OnRspQueryMaxOrderVolume(self, pQueryMaxOrderVolume, pRspInfo, nRequestID, bIsLast):
        log.debug("OnRspQueryMaxOrderVolume", pQueryMaxOrderVolume, pRspInfo, nRequestID, bIsLast)

    def OnRspRemoveParkedOrder(self, pRemoveParkedOrder, pRspInfo, nRequestID, bIsLast):
        log.debug("OnRspRemoveParkedOrder", pRemoveParkedOrder, pRspInfo, nRequestID, bIsLast)

    def OnRspRemoveParkedOrderAction(self, pRemoveParkedOrderAction, pRspInfo, nRequestID, bIsLast):
        log.debug("OnRspRemoveParkedOrderAction", pRemoveParkedOrderAction, pRspInfo, nRequestID, bIsLast)

    def OnRspSettlementInfoConfirm(self, pSettlementInfoConfirm, pRspInfo, nRequestID, bIsLast):
        log.debug("OnRspSettlementInfoConfirm", pSettlementInfoConfirm, pRspInfo, nRequestID, bIsLast)

    def OnRspTradingAccountPasswordUpdate(self, pTradingAccountPasswordUpdate, pRspInfo, nRequestID, bIsLast):
        log.debug("OnRspTradingAccountPasswordUpdate", pTradingAccountPasswordUpdate, pRspInfo, nRequestID, bIsLast)

    def OnRspUserLogin(self, pRspUserLogin, pRspInfo, nRequestID, bIsLast):
        log.debug("OnRspUserLogin", pRspUserLogin, pRspInfo, nRequestID, bIsLast)

    def OnRspUserLogout(self, pUserLogout, pRspInfo, nRequestID, bIsLast):
        log.debug("OnRspUserLogout", pUserLogout, pRspInfo, nRequestID, bIsLast)

    def OnRspUserPasswordUpdate(self, pUserPasswordUpdate, pRspInfo, nRequestID, bIsLast):
        log.debug("OnRspUserPasswordUpdate", pUserPasswordUpdate, pRspInfo, nRequestID, bIsLast)

    def OnRtnCFMMCTradingAccountToken(self, pCFMMCTradingAccountToken):
        log.debug("OnRtnCFMMCTradingAccountToken", pCFMMCTradingAccountToken)

    def OnRtnCancelAccountByBank(self, pCancelAccount):
        log.debug("OnRtnCancelAccountByBank", pCancelAccount)

    def OnRtnChangeAccountByBank(self, pChangeAccount):
        log.debug("OnRtnChangeAccountByBank", pChangeAccount)

    def OnRtnErrorConditionalOrder(self, pErrorConditionalOrder):
        log.debug("OnRtnErrorConditionalOrder", pErrorConditionalOrder)

    def OnRtnFromBankToFutureByBank(self, pRspTransfer):
        log.debug("OnRtnFromBankToFutureByBank", pRspTransfer)

    def OnRtnFromBankToFutureByFuture(self, pRspTransfer):
        log.debug("OnRtnFromBankToFutureByFuture", pRspTransfer)

    def OnRtnFromFutureToBankByBank(self, pRspTransfer):
        log.debug("OnRtnFromFutureToBankByBank", pRspTransfer)

    def OnRtnFromFutureToBankByFuture(self, pRspTransfer):
        log.debug("OnRtnFromFutureToBankByFuture", pRspTransfer)

    def OnRtnInstrumentStatus(self, pInstrumentStatus):
        log.debug("OnRtnInstrumentStatus", pInstrumentStatus)

    def OnRtnOpenAccountByBank(self, pOpenAccount):
        log.debug("OnRtnOpenAccountByBank", pOpenAccount)

    def OnRtnOrder(self, pOrder):
        log.debug("OnRtnOrder", pOrder)

    def OnRtnQueryBankBalanceByFuture(self, pNotifyQueryAccount):
        log.debug("OnRtnQueryBankBalanceByFuture", pNotifyQueryAccount)

    def OnRtnRepealFromBankToFutureByBank(self, pRspRepeal):
        log.debug("OnRtnRepealFromBankToFutureByBank", pRspRepeal)

    def OnRtnRepealFromBankToFutureByFuture(self, pRspRepeal):
        log.debug("OnRtnRepealFromBankToFutureByFuture", pRspRepeal)

    def OnRtnRepealFromBankToFutureByFutureManual(self, pRspRepeal):
        log.debug("OnRtnRepealFromBankToFutureByFutureManual", pRspRepeal)

    def OnRtnRepealFromFutureToBankByBank(self, pRspRepeal):
        log.debug("OnRtnRepealFromFutureToBankByBank", pRspRepeal)

    def OnRtnRepealFromFutureToBankByFuture(self, pRspRepeal):
        log.debug("OnRtnRepealFromFutureToBankByFuture", pRspRepeal)

    def OnRtnRepealFromFutureToBankByFutureManual(self, pRspRepeal):
        log.debug("OnRtnRepealFromFutureToBankByFutureManual", pRspRepeal)

    def OnRtnTrade(self, pTrade):
        log.debug("OnRtnTrade", pTrade)

    def OnRtnTradingNotice(self, pTradingNoticeInfo):
        log.debug("OnRtnTradingNotice", pTradingNoticeInfo)
    def myReqAuthenticate(self, *args, **kwargs):
        log.debug("myReqAuthenticate")
        self.requestID++
        pReqAuthenticate = ApiStruct.ReqAuthenticate(**kwargs)
        pReqAuthenticate.BrokerID = self.BrokerID
        pReqAuthenticate.InvestorID= self.InvestorID
        self.ReqAuthenticate(pReqAuthenticate, self.requestID):

    def myReqFromBankToFutureByFuture(self, *args, **kwargs):
        log.debug("myReqFromBankToFutureByFuture")
        self.requestID++
        pReqTransfer = ApiStruct.ReqTransfer(**kwargs)
        pReqTransfer.BrokerID = self.BrokerID
        pReqTransfer.InvestorID= self.InvestorID
        self.ReqFromBankToFutureByFuture(pReqTransfer, self.requestID):

    def myReqFromFutureToBankByFuture(self, *args, **kwargs):
        log.debug("myReqFromFutureToBankByFuture")
        self.requestID++
        pReqTransfer = ApiStruct.ReqTransfer(**kwargs)
        pReqTransfer.BrokerID = self.BrokerID
        pReqTransfer.InvestorID= self.InvestorID
        self.ReqFromFutureToBankByFuture(pReqTransfer, self.requestID):

    def myReqOrderAction(self, *args, **kwargs):
        log.debug("myReqOrderAction")
        self.requestID++
        pInputOrderAction = ApiStruct.InputOrderAction(**kwargs)
        pInputOrderAction.BrokerID = self.BrokerID
        pInputOrderAction.InvestorID= self.InvestorID
        self.ReqOrderAction(pInputOrderAction, self.requestID):

    def myReqOrderInsert(self, *args, **kwargs):
        log.debug("myReqOrderInsert")
        self.requestID++
        pInputOrder = ApiStruct.InputOrder(**kwargs)
        pInputOrder.BrokerID = self.BrokerID
        pInputOrder.InvestorID= self.InvestorID
        self.ReqOrderInsert(pInputOrder, self.requestID):

    def myReqParkedOrderAction(self, *args, **kwargs):
        log.debug("myReqParkedOrderAction")
        self.requestID++
        pParkedOrderAction = ApiStruct.ParkedOrderAction(**kwargs)
        pParkedOrderAction.BrokerID = self.BrokerID
        pParkedOrderAction.InvestorID= self.InvestorID
        self.ReqParkedOrderAction(pParkedOrderAction, self.requestID):

    def myReqParkedOrderInsert(self, *args, **kwargs):
        log.debug("myReqParkedOrderInsert")
        self.requestID++
        pParkedOrder = ApiStruct.ParkedOrder(**kwargs)
        pParkedOrder.BrokerID = self.BrokerID
        pParkedOrder.InvestorID= self.InvestorID
        self.ReqParkedOrderInsert(pParkedOrder, self.requestID):

    def myReqQryAccountregister(self, *args, **kwargs):
        log.debug("myReqQryAccountregister")
        self.requestID++
        pQryAccountregister = ApiStruct.QryAccountregister(**kwargs)
        pQryAccountregister.BrokerID = self.BrokerID
        pQryAccountregister.InvestorID= self.InvestorID
        self.ReqQryAccountregister(pQryAccountregister, self.requestID):

    def myReqQryBrokerTradingAlgos(self, *args, **kwargs):
        log.debug("myReqQryBrokerTradingAlgos")
        self.requestID++
        pQryBrokerTradingAlgos = ApiStruct.QryBrokerTradingAlgos(**kwargs)
        pQryBrokerTradingAlgos.BrokerID = self.BrokerID
        pQryBrokerTradingAlgos.InvestorID= self.InvestorID
        self.ReqQryBrokerTradingAlgos(pQryBrokerTradingAlgos, self.requestID):

    def myReqQryBrokerTradingParams(self, *args, **kwargs):
        log.debug("myReqQryBrokerTradingParams")
        self.requestID++
        pQryBrokerTradingParams = ApiStruct.QryBrokerTradingParams(**kwargs)
        pQryBrokerTradingParams.BrokerID = self.BrokerID
        pQryBrokerTradingParams.InvestorID= self.InvestorID
        self.ReqQryBrokerTradingParams(pQryBrokerTradingParams, self.requestID):

    def myReqQryCFMMCTradingAccountKey(self, *args, **kwargs):
        log.debug("myReqQryCFMMCTradingAccountKey")
        self.requestID++
        pQryCFMMCTradingAccountKey = ApiStruct.QryCFMMCTradingAccountKey(**kwargs)
        pQryCFMMCTradingAccountKey.BrokerID = self.BrokerID
        pQryCFMMCTradingAccountKey.InvestorID= self.InvestorID
        self.ReqQryCFMMCTradingAccountKey(pQryCFMMCTradingAccountKey, self.requestID):

    def myReqQryContractBank(self, *args, **kwargs):
        log.debug("myReqQryContractBank")
        self.requestID++
        pQryContractBank = ApiStruct.QryContractBank(**kwargs)
        pQryContractBank.BrokerID = self.BrokerID
        pQryContractBank.InvestorID= self.InvestorID
        self.ReqQryContractBank(pQryContractBank, self.requestID):

    def myReqQryDepthMarketData(self, *args, **kwargs):
        log.debug("myReqQryDepthMarketData")
        self.requestID++
        pQryDepthMarketData = ApiStruct.QryDepthMarketData(**kwargs)
        pQryDepthMarketData.BrokerID = self.BrokerID
        pQryDepthMarketData.InvestorID= self.InvestorID
        self.ReqQryDepthMarketData(pQryDepthMarketData, self.requestID):

    def myReqQryEWarrantOffset(self, *args, **kwargs):
        log.debug("myReqQryEWarrantOffset")
        self.requestID++
        pQryEWarrantOffset = ApiStruct.QryEWarrantOffset(**kwargs)
        pQryEWarrantOffset.BrokerID = self.BrokerID
        pQryEWarrantOffset.InvestorID= self.InvestorID
        self.ReqQryEWarrantOffset(pQryEWarrantOffset, self.requestID):

    def myReqQryExchange(self, *args, **kwargs):
        log.debug("myReqQryExchange")
        self.requestID++
        pQryExchange = ApiStruct.QryExchange(**kwargs)
        pQryExchange.BrokerID = self.BrokerID
        pQryExchange.InvestorID= self.InvestorID
        self.ReqQryExchange(pQryExchange, self.requestID):

    def myReqQryExchangeMarginRate(self, *args, **kwargs):
        log.debug("myReqQryExchangeMarginRate")
        self.requestID++
        pQryExchangeMarginRate = ApiStruct.QryExchangeMarginRate(**kwargs)
        pQryExchangeMarginRate.BrokerID = self.BrokerID
        pQryExchangeMarginRate.InvestorID= self.InvestorID
        self.ReqQryExchangeMarginRate(pQryExchangeMarginRate, self.requestID):

    def myReqQryExchangeMarginRateAdjust(self, *args, **kwargs):
        log.debug("myReqQryExchangeMarginRateAdjust")
        self.requestID++
        pQryExchangeMarginRateAdjust = ApiStruct.QryExchangeMarginRateAdjust(**kwargs)
        pQryExchangeMarginRateAdjust.BrokerID = self.BrokerID
        pQryExchangeMarginRateAdjust.InvestorID= self.InvestorID
        self.ReqQryExchangeMarginRateAdjust(pQryExchangeMarginRateAdjust, self.requestID):

    def myReqQryExchangeRate(self, *args, **kwargs):
        log.debug("myReqQryExchangeRate")
        self.requestID++
        pQryExchangeRate = ApiStruct.QryExchangeRate(**kwargs)
        pQryExchangeRate.BrokerID = self.BrokerID
        pQryExchangeRate.InvestorID= self.InvestorID
        self.ReqQryExchangeRate(pQryExchangeRate, self.requestID):

    def myReqQryInstrument(self, *args, **kwargs):
        log.debug("myReqQryInstrument")
        self.requestID++
        pQryInstrument = ApiStruct.QryInstrument(**kwargs)
        pQryInstrument.BrokerID = self.BrokerID
        pQryInstrument.InvestorID= self.InvestorID
        self.ReqQryInstrument(pQryInstrument, self.requestID):

    def myReqQryInstrumentCommissionRate(self, *args, **kwargs):
        log.debug("myReqQryInstrumentCommissionRate")
        self.requestID++
        pQryInstrumentCommissionRate = ApiStruct.QryInstrumentCommissionRate(**kwargs)
        pQryInstrumentCommissionRate.BrokerID = self.BrokerID
        pQryInstrumentCommissionRate.InvestorID= self.InvestorID
        self.ReqQryInstrumentCommissionRate(pQryInstrumentCommissionRate, self.requestID):

    def myReqQryInstrumentMarginRate(self, *args, **kwargs):
        log.debug("myReqQryInstrumentMarginRate")
        self.requestID++
        pQryInstrumentMarginRate = ApiStruct.QryInstrumentMarginRate(**kwargs)
        pQryInstrumentMarginRate.BrokerID = self.BrokerID
        pQryInstrumentMarginRate.InvestorID= self.InvestorID
        self.ReqQryInstrumentMarginRate(pQryInstrumentMarginRate, self.requestID):

    def myReqQryInvestor(self, *args, **kwargs):
        log.debug("myReqQryInvestor")
        self.requestID++
        pQryInvestor = ApiStruct.QryInvestor(**kwargs)
        pQryInvestor.BrokerID = self.BrokerID
        pQryInvestor.InvestorID= self.InvestorID
        self.ReqQryInvestor(pQryInvestor, self.requestID):

    def myReqQryInvestorPosition(self, *args, **kwargs):
        log.debug("myReqQryInvestorPosition")
        self.requestID++
        pQryInvestorPosition = ApiStruct.QryInvestorPosition(**kwargs)
        pQryInvestorPosition.BrokerID = self.BrokerID
        pQryInvestorPosition.InvestorID= self.InvestorID
        self.ReqQryInvestorPosition(pQryInvestorPosition, self.requestID):

    def myReqQryInvestorPositionCombineDetail(self, *args, **kwargs):
        log.debug("myReqQryInvestorPositionCombineDetail")
        self.requestID++
        pQryInvestorPositionCombineDetail = ApiStruct.QryInvestorPositionCombineDetail(**kwargs)
        pQryInvestorPositionCombineDetail.BrokerID = self.BrokerID
        pQryInvestorPositionCombineDetail.InvestorID= self.InvestorID
        self.ReqQryInvestorPositionCombineDetail(pQryInvestorPositionCombineDetail, self.requestID):

    def myReqQryInvestorPositionDetail(self, *args, **kwargs):
        log.debug("myReqQryInvestorPositionDetail")
        self.requestID++
        pQryInvestorPositionDetail = ApiStruct.QryInvestorPositionDetail(**kwargs)
        pQryInvestorPositionDetail.BrokerID = self.BrokerID
        pQryInvestorPositionDetail.InvestorID= self.InvestorID
        self.ReqQryInvestorPositionDetail(pQryInvestorPositionDetail, self.requestID):

    def myReqQryInvestorProductGroupMargin(self, *args, **kwargs):
        log.debug("myReqQryInvestorProductGroupMargin")
        self.requestID++
        pQryInvestorProductGroupMargin = ApiStruct.QryInvestorProductGroupMargin(**kwargs)
        pQryInvestorProductGroupMargin.BrokerID = self.BrokerID
        pQryInvestorProductGroupMargin.InvestorID= self.InvestorID
        self.ReqQryInvestorProductGroupMargin(pQryInvestorProductGroupMargin, self.requestID):

    def myReqQryNotice(self, *args, **kwargs):
        log.debug("myReqQryNotice")
        self.requestID++
        pQryNotice = ApiStruct.QryNotice(**kwargs)
        pQryNotice.BrokerID = self.BrokerID
        pQryNotice.InvestorID= self.InvestorID
        self.ReqQryNotice(pQryNotice, self.requestID):

    def myReqQryOrder(self, *args, **kwargs):
        log.debug("myReqQryOrder")
        self.requestID++
        pQryOrder = ApiStruct.QryOrder(**kwargs)
        pQryOrder.BrokerID = self.BrokerID
        pQryOrder.InvestorID= self.InvestorID
        self.ReqQryOrder(pQryOrder, self.requestID):

    def myReqQryParkedOrder(self, *args, **kwargs):
        log.debug("myReqQryParkedOrder")
        self.requestID++
        pQryParkedOrder = ApiStruct.QryParkedOrder(**kwargs)
        pQryParkedOrder.BrokerID = self.BrokerID
        pQryParkedOrder.InvestorID= self.InvestorID
        self.ReqQryParkedOrder(pQryParkedOrder, self.requestID):

    def myReqQryParkedOrderAction(self, *args, **kwargs):
        log.debug("myReqQryParkedOrderAction")
        self.requestID++
        pQryParkedOrderAction = ApiStruct.QryParkedOrderAction(**kwargs)
        pQryParkedOrderAction.BrokerID = self.BrokerID
        pQryParkedOrderAction.InvestorID= self.InvestorID
        self.ReqQryParkedOrderAction(pQryParkedOrderAction, self.requestID):

    def myReqQryProduct(self, *args, **kwargs):
        log.debug("myReqQryProduct")
        self.requestID++
        pQryProduct = ApiStruct.QryProduct(**kwargs)
        pQryProduct.BrokerID = self.BrokerID
        pQryProduct.InvestorID= self.InvestorID
        self.ReqQryProduct(pQryProduct, self.requestID):

    def myReqQrySecAgentACIDMap(self, *args, **kwargs):
        log.debug("myReqQrySecAgentACIDMap")
        self.requestID++
        pQrySecAgentACIDMap = ApiStruct.QrySecAgentACIDMap(**kwargs)
        pQrySecAgentACIDMap.BrokerID = self.BrokerID
        pQrySecAgentACIDMap.InvestorID= self.InvestorID
        self.ReqQrySecAgentACIDMap(pQrySecAgentACIDMap, self.requestID):

    def myReqQrySettlementInfo(self, *args, **kwargs):
        log.debug("myReqQrySettlementInfo")
        self.requestID++
        pQrySettlementInfo = ApiStruct.QrySettlementInfo(**kwargs)
        pQrySettlementInfo.BrokerID = self.BrokerID
        pQrySettlementInfo.InvestorID= self.InvestorID
        self.ReqQrySettlementInfo(pQrySettlementInfo, self.requestID):

    def myReqQrySettlementInfoConfirm(self, *args, **kwargs):
        log.debug("myReqQrySettlementInfoConfirm")
        self.requestID++
        pQrySettlementInfoConfirm = ApiStruct.QrySettlementInfoConfirm(**kwargs)
        pQrySettlementInfoConfirm.BrokerID = self.BrokerID
        pQrySettlementInfoConfirm.InvestorID= self.InvestorID
        self.ReqQrySettlementInfoConfirm(pQrySettlementInfoConfirm, self.requestID):

    def myReqQryTrade(self, *args, **kwargs):
        log.debug("myReqQryTrade")
        self.requestID++
        pQryTrade = ApiStruct.QryTrade(**kwargs)
        pQryTrade.BrokerID = self.BrokerID
        pQryTrade.InvestorID= self.InvestorID
        self.ReqQryTrade(pQryTrade, self.requestID):

    def myReqQryTradingAccount(self, *args, **kwargs):
        log.debug("myReqQryTradingAccount")
        self.requestID++
        pQryTradingAccount = ApiStruct.QryTradingAccount(**kwargs)
        pQryTradingAccount.BrokerID = self.BrokerID
        pQryTradingAccount.InvestorID= self.InvestorID
        self.ReqQryTradingAccount(pQryTradingAccount, self.requestID):

    def myReqQryTradingCode(self, *args, **kwargs):
        log.debug("myReqQryTradingCode")
        self.requestID++
        pQryTradingCode = ApiStruct.QryTradingCode(**kwargs)
        pQryTradingCode.BrokerID = self.BrokerID
        pQryTradingCode.InvestorID= self.InvestorID
        self.ReqQryTradingCode(pQryTradingCode, self.requestID):

    def myReqQryTradingNotice(self, *args, **kwargs):
        log.debug("myReqQryTradingNotice")
        self.requestID++
        pQryTradingNotice = ApiStruct.QryTradingNotice(**kwargs)
        pQryTradingNotice.BrokerID = self.BrokerID
        pQryTradingNotice.InvestorID= self.InvestorID
        self.ReqQryTradingNotice(pQryTradingNotice, self.requestID):

    def myReqQryTransferBank(self, *args, **kwargs):
        log.debug("myReqQryTransferBank")
        self.requestID++
        pQryTransferBank = ApiStruct.QryTransferBank(**kwargs)
        pQryTransferBank.BrokerID = self.BrokerID
        pQryTransferBank.InvestorID= self.InvestorID
        self.ReqQryTransferBank(pQryTransferBank, self.requestID):

    def myReqQryTransferSerial(self, *args, **kwargs):
        log.debug("myReqQryTransferSerial")
        self.requestID++
        pQryTransferSerial = ApiStruct.QryTransferSerial(**kwargs)
        pQryTransferSerial.BrokerID = self.BrokerID
        pQryTransferSerial.InvestorID= self.InvestorID
        self.ReqQryTransferSerial(pQryTransferSerial, self.requestID):

    def myReqQueryBankAccountMoneyByFuture(self, *args, **kwargs):
        log.debug("myReqQueryBankAccountMoneyByFuture")
        self.requestID++
        pReqQueryAccount = ApiStruct.ReqQueryAccount(**kwargs)
        pReqQueryAccount.BrokerID = self.BrokerID
        pReqQueryAccount.InvestorID= self.InvestorID
        self.ReqQueryBankAccountMoneyByFuture(pReqQueryAccount, self.requestID):

    def myReqQueryCFMMCTradingAccountToken(self, *args, **kwargs):
        log.debug("myReqQueryCFMMCTradingAccountToken")
        self.requestID++
        pQueryCFMMCTradingAccountToken = ApiStruct.QueryCFMMCTradingAccountToken(**kwargs)
        pQueryCFMMCTradingAccountToken.BrokerID = self.BrokerID
        pQueryCFMMCTradingAccountToken.InvestorID= self.InvestorID
        self.ReqQueryCFMMCTradingAccountToken(pQueryCFMMCTradingAccountToken, self.requestID):

    def myReqQueryMaxOrderVolume(self, *args, **kwargs):
        log.debug("myReqQueryMaxOrderVolume")
        self.requestID++
        pQueryMaxOrderVolume = ApiStruct.QueryMaxOrderVolume(**kwargs)
        pQueryMaxOrderVolume.BrokerID = self.BrokerID
        pQueryMaxOrderVolume.InvestorID= self.InvestorID
        self.ReqQueryMaxOrderVolume(pQueryMaxOrderVolume, self.requestID):

    def myReqRemoveParkedOrder(self, *args, **kwargs):
        log.debug("myReqRemoveParkedOrder")
        self.requestID++
        pRemoveParkedOrder = ApiStruct.RemoveParkedOrder(**kwargs)
        pRemoveParkedOrder.BrokerID = self.BrokerID
        pRemoveParkedOrder.InvestorID= self.InvestorID
        self.ReqRemoveParkedOrder(pRemoveParkedOrder, self.requestID):

    def myReqRemoveParkedOrderAction(self, *args, **kwargs):
        log.debug("myReqRemoveParkedOrderAction")
        self.requestID++
        pRemoveParkedOrderAction = ApiStruct.RemoveParkedOrderAction(**kwargs)
        pRemoveParkedOrderAction.BrokerID = self.BrokerID
        pRemoveParkedOrderAction.InvestorID= self.InvestorID
        self.ReqRemoveParkedOrderAction(pRemoveParkedOrderAction, self.requestID):

    def myReqSettlementInfoConfirm(self, *args, **kwargs):
        log.debug("myReqSettlementInfoConfirm")
        self.requestID++
        pSettlementInfoConfirm = ApiStruct.SettlementInfoConfirm(**kwargs)
        pSettlementInfoConfirm.BrokerID = self.BrokerID
        pSettlementInfoConfirm.InvestorID= self.InvestorID
        self.ReqSettlementInfoConfirm(pSettlementInfoConfirm, self.requestID):

    def myReqTradingAccountPasswordUpdate(self, *args, **kwargs):
        log.debug("myReqTradingAccountPasswordUpdate")
        self.requestID++
        pTradingAccountPasswordUpdate = ApiStruct.TradingAccountPasswordUpdate(**kwargs)
        pTradingAccountPasswordUpdate.BrokerID = self.BrokerID
        pTradingAccountPasswordUpdate.InvestorID= self.InvestorID
        self.ReqTradingAccountPasswordUpdate(pTradingAccountPasswordUpdate, self.requestID):

    def myReqUserLogin(self, *args, **kwargs):
        log.debug("myReqUserLogin")
        self.requestID++
        pReqUserLogin = ApiStruct.ReqUserLogin(**kwargs)
        pReqUserLogin.BrokerID = self.BrokerID
        pReqUserLogin.InvestorID= self.InvestorID
        self.ReqUserLogin(pReqUserLogin, self.requestID):

    def myReqUserLogout(self, *args, **kwargs):
        log.debug("myReqUserLogout")
        self.requestID++
        pUserLogout = ApiStruct.UserLogout(**kwargs)
        pUserLogout.BrokerID = self.BrokerID
        pUserLogout.InvestorID= self.InvestorID
        self.ReqUserLogout(pUserLogout, self.requestID):

    def myReqUserPasswordUpdate(self, *args, **kwargs):
        log.debug("myReqUserPasswordUpdate")
        self.requestID++
        pUserPasswordUpdate = ApiStruct.UserPasswordUpdate(**kwargs)
        pUserPasswordUpdate.BrokerID = self.BrokerID
        pUserPasswordUpdate.InvestorID= self.InvestorID
        self.ReqUserPasswordUpdate(pUserPasswordUpdate, self.requestID):

