# https://api.xt.com/data/api/v1/getDepth?market=btc_usdt
"""
{
 "time":1662075535225,
 "last":"20107.13",
 "asks":[
   [20107.13,1.783141],
   [20107.45,0.02813],
   [20107.57,2.374841],
   [20107.72,3.795289],
"""


from xtdotcomv1.utils import process_response
from xtdotcomv1.api_general import ApiGeneral

import requests 
import json
import pandas as pd



class LimitOrders(ApiGeneral):
  def __init__(self, symbol):
    super().__init__()
    
    session = requests.Session()
    session.trust_env = False
    self.session = session

    self.symbol = symbol
    self.url_limit_orders = self.base_url + '/data/api/v1/getDepth?market=' + self.symbol
  
  
  def getLimitOrders(self):
    responseObj = self.session.get(self.url_limit_orders) 
    return responseObj

  def processResponseLimitOrders(self):
    responseObj = self.getLimitOrders()
    msgJson = process_response.processResponse(responseObj)
    return msgJson

  def processJsonLimitOrders(self):
    msgJson = self.processResponseLimitOrders()
    
    rowJson0 = msgJson['bids']
    df0_bids = pd.DataFrame(rowJson0)
    df0_bids.rename(columns = {0: 'price', 1: 'quantity'}, inplace = True)
    df0_bids['price'] = df0_bids['price'].astype(float)
    df0_bids['quantity'] = df0_bids['quantity'].astype(float)
    df_bids = df0_bids.groupby(['price']).quantity.sum().reset_index()
    df_bids = df_bids.sort_values(by='price', ascending=False)
    df_bids.reset_index(inplace=True, drop=True)
    
    rowJson1 = msgJson['asks']
    df0_asks = pd.DataFrame(rowJson1)
    df0_asks.rename(columns = {0: 'price', 1: 'quantity'}, inplace = True)
    df0_asks['price'] = df0_asks['price'].astype(float)
    df0_asks['quantity'] = df0_asks['quantity'].astype(float)
    df_asks = df0_asks.groupby(['price']).quantity.sum().reset_index()
    
    return df_bids, df_asks
    

"""
import numpy as np
from xtdotcomv1.public.limit_orders import LimitOrders
lo = LimitOrders("btc_usdt")
lo_data = lo.processJsonLimitOrders()
"""
