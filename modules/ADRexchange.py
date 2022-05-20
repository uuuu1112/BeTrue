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

