import requests
import pandas as pd
from modules import Common
from modules import Datetime

earnDate=Datetime.EarnDate()
dateManage=Datetime.DateManage()
url = "https://api.finmindtrade.com/api/v4/data"
Today=Datetime.Today

class DateMange():
    def nYearDate(self,n=1,date=Today):
        earningReleaseDate=earnDate.earningReleaseDate(date)
        nYearDate=dateManage.nYearRelease(n,earningReleaseDate)
        return nYearDate

class getInfo():
    def nYearData(self,n=1,date=Today):
        content=[]
        nYearDate=self.nYearData(n,date)
        for date in nYearDate:
            parameter = {
            "dataset": "TaiwanStockFinancialStatements",
            "start_date": date,
            "token": Common.token}
            data=Common.toPd(url,parameter)
            content.append(data)
        data=pd.concat(content)
        return data