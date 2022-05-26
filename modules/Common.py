import requests
import pandas as pd

token="eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJkYXRlIjoiMjAyMi0wNS0yNCAxNDoyMjo1NyIsInVzZXJfaWQiOiJ1dXV1MTExMiIsImlwIjoiNjAuMjQ5LjE4MC4yMDAifQ.qQdzvWhSPBs5qttIge-e2fF9nkkj3r38owgwpKht4m8"

def toPd(url,parameter):
    data=requests.get(url,params=parameter)
    data=data.json()
    data=pd.DataFrame(data['data'])
    return data