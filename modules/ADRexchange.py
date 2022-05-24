import Common
import Datetime
import pandas as pd

# before days
beforeDays=Datetime.beforeDays(2)

# exchange rate pd
exchangeurl="https://api.finmindtrade.com/api/v4/data"
exchangeParam={
    "dataset": "TaiwanExchangeRate",
    "data_id": "USD",
    "start_date":beforeDays
}
exchange=Common.toPd(exchangeurl,exchangeParam)

#adrlist
adrMap={"TSM":"2330","UMC":"2303","CHT":"2412","ASX":"3711","IMOS":"8150"}

#adr multiple list
changeMul={
    "stock_id":["2330","2303","2412","3711","8150"],
    "換股數":[5,5,10,2,20]      
          }
changeMul=pd.DataFrame(changeMul)

# for item in adrList concat item
def concatADR(beforeDays):
    adrInfo=[]
    twstockInfo=[]
    adrurl="https://api.finmindtrade.com/api/v3/data"
    twstockurl="https://api.finmindtrade.com/api/v4/data"
    adrParam={
        "dataset": "USStockPrice",
        "stock_id": item,
        "date": beforeDays,
    }
    twstockParam={
        "dataset": "TaiwanStockPrice",
        "data_id": adrMap[item],
        "start_date": beforeDays,
        "token": "", # 參考登入，獲取金鑰
    }
    for item in adrMap:
        adrItem=Common.toPd(adrurl,adrParam)
        adrInfo.append(adrItem)
        twstock=Common.toPd(twstockurl,twstockParam)
        twstockInfo.append(twstock)
    adrInfo=pd.concat(adrInfo)
    adrInfo['stock_id']=adrInfo['stock_id'].map(adrMap)
    twstockInfo=pd.concat(twstockInfo)

    #組合data
    adrCompare=pd.merge(twstockInfo,adrInfo,how="outer")
    adrCompare=pd.merge(adrCompare,exchange,how="outer")
    adrCompare=pd.merge(adrCompare,changeMul,how="outer")

    adrCompare['ADR換算']=adrCompare.Close/adrCompare.換股數*(adrCompare.spot_buy+adrCompare.spot_sell)/2
    adrCompare['ADR溢價']=((adrCompare.ADR換算-adrCompare.close)/adrCompare.close).apply(lambda x:format(x,'.2%'))