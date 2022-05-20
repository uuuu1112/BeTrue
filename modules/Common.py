import requests
import pandas as pd

def toPd(url,parameter):
    data=requests.get(url,params=parameter)
    data=data.json()
    data=pd.DataFrame(data['data'])
    return data