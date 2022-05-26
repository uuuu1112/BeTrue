import datetime
from datetime import datetime
from dateutil.relativedelta import relativedelta

    
Today=datetime.today().strftime("%Y-%m-%d")
earningRelease=['5-15','8-14','11-14','3-31'] 
earningQtrDate=['3-31','06-30','09-30','12-31']

class DateManage:
    # 把財報發布的日期換算成天數
    def earnReleasePoint(self):
        content=[]
        for item in earningRelease:
            date=datetime.strptime(item,"%m-%d")
            point=date.month*30+date.day
            content.append(point)
        return content
    # 一個月前的日期
    def monthsBefore(self,n,today=Today):
        today=datetime.strptime(today,"%Y-%m-%d")
        return (today- relativedelta(months=n)).strftime("%Y-%m-%d")
    # 一年前的日期
    def yearsBefore(self,n,today=Today):
        today=datetime.strptime(today,"%Y-%m-%d")
        return (today- relativedelta(years=n)).strftime("%Y-%m-%d")
    #回傳n年的資料
    def nYearRelease(self,N,list):
        content=[]
        for n in range(N):
            for item in list:
                content.append(self.yearsBefore(n,item))
        return content

class RevenueDate(DateManage):
    # 找出最近的營收發布日
    def revenueRelease(self,today=Today):
        today=datetime.strptime(today,"%Y-%m-%d")
        if today.day>15:
            return today.replace(day=15).strftime("%Y-%m-%d")
        else:
            today.replace(month=today.month-1)
            return today.replace(day=15).strftime("%Y-%m-%d")
    #回傳近12個月的月營收日期
    def revenue12Release(self,today=Today):
        content=[]
        releaseDate=self.revenueRelease(today)
        for i in range(12):
            content.append(self.monthsBefore(i,releaseDate))
        return content


class EarnDate(DateManage):
    # 對應第幾季
    def checkSeason(self,today=Today):
        today=datetime.strptime(today,"%Y-%m-%d")
        checkPoint=today.month*30+today.day
        if checkPoint>=self.earnReleasePoint()[0] and checkPoint<self.earnReleasePoint()[1]:
            return 1
        elif checkPoint>=self.earnReleasePoint()[1] and checkPoint<self.earnReleasePoint()[2]:
            return 2
        elif checkPoint>=self.earnReleasePoint()[2] and checkPoint<self.earnReleasePoint()[3]:
            return 3
        else:
            return 4
    # 最近四季的財報發布日
    def earningReleaseDate(self,today=Today):
        content=[]
        for i in range(4):
            if i>=self.checkSeason(today):
                earningReleaseConvert=str(datetime.today().year-1)+"-"+earningQtrDate[i]
                content.append(earningReleaseConvert)
        for i in range(4):
            if i<self.checkSeason(today):
                earningReleaseConvert=str(datetime.today().year)+"-"+earningQtrDate[i]
                content.append(earningReleaseConvert)
        return content