import datetime
import shioaji as sj
import pandas as pd
from dotenv import load_dotenv
import os

load_dotenv('account.env')
api = sj.Shioaji()
accounts = api.login(os.getenv('ACCOUNT'), os.getenv('PASS'))
"""
api.activate_ca(
    ca_path=r"Sinopac.pfx",
    ca_passwd="D122759551",
    person_id="D122759551",
)

tws = api.Contracts.Indexs.TSE.TSE001
print (tws)

kbars = api.kbars(tws, start="2020-09-18", end="2020-09-18")
data = pd.DataFrame({**kbars})
data.ts = pd.to_datetime(data.ts)
data.head()
contract_0050 = api.Contracts.Stocks["0050"]
ticks = api.ticks(contract_0050, "2020-09-18")
data = pd.DataFrame({**ticks})
data.ts = pd.to_datetime(data.ts)
data.head()
print (data)
"""

# 1-3: 表示結算週別 TX1, TX2, TXO, TX4, TX5 (其中第三週改為月選擇權 TXO)
# Taiwan option : TX + [WEEK] + [履約價] + [MONTH] + [202[0]], EX : TXO18000L0 
# CALL -> MONTH 1 : A, 2 : B, 3 : C ..... ('A' + current month - 1)
# PUT  -> MONTH 1 : M, 2 : N, 3 : P ..... ('M' + current month - 1)

#Task 1 : 距離到期日幾天會發生最大跌幅

op = api.Contracts.Options.TXO.TXO202202018300P
print(op)
api.logout()
# sma cross strategy