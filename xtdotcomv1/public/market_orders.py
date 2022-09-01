# https://api.xt.com/data/api/v1/getTrades?market=btc_usdt
"""
[
[1662075590915,20107.49,0.903686,"ask","6971250298849331202"],
[1662075590173,20107.49,0.024026,"ask","6971250295737157634"],
"""


from xtdotcomv1.utils import process_response
from xtdotcomv1.api_general import ApiGeneral

import requests 
import json
import pandas as pd


class MarketOrders(ApiGeneral):
  def __init__(self, symbol):
    super().__init__()
    
    session = requests.Session()
    session.trust_env = False
    self.session = session

    self.symbol = symbol
    self.url_market_orders = self.base_url + '/data/api/v1/getTrades?market=' + self.symbol
  
  
  def getMarketOrders(self):
    responseObj = self.session.get(self.url_market_orders) 
    return responseObj

  def processResponseMarketOrders(self):
    responseObj = self.getMarketOrders()
    msgJson = process_response.processResponse(responseObj)
    return msgJson

  def processJsonMarketOrders(self):
    msgJson = self.processResponseMarketOrders()
    df = pd.DataFrame(msgJson)
    # [Timestamp, deal price, volume, Transaction type, Record ID]
    # Trading type [bid:buy, ask:sell]
    # df0_bids.rename(columns = {0: 'price', 1: 'quantity'}, inplace = True)
    
    df.rename(columns = {0: 'timestamp', 1: 'price', 2: 'size', 3: 'type', 4: 'id'}, inplace=True)
    df['timestamp'] = df['timestamp'].astype(int)
    df['price'] = df['price'].astype(float)
    df['size'] = df['size'].astype(float)
    
    df['direction'] = df.apply(lambda row: 1 if row.type=='bid' else -1, axis=1)
    df['quantity'] = df['size']*df['direction'] 
    df.timestamp = pd.to_datetime(df.timestamp)
    df = df.sort_values(by='timestamp')
    df.reset_index(inplace=True, drop=True)
    return df


"""
import numpy as np
from xtdotcomv1.public.market_orders import MarketOrders
mo = MarketOrders("btc_usdt")
mo_data = mo.processJsonMarketOrders()
"""
