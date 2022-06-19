import pandas as pd

from xtdotcomv1 .private.get_positions import GetPositions
from xtdotcomv1.private.get_orders import GetOrders
from xtdotcomv1.private.cancel_order import CancelOrder
from xtdotcomv1.private.create_order import CreateOrder





API_KEY_FILE = 'C:\\Me\\Crypto\\Trading\\xtdotcomv1\\api_key.txt';  
API_SECRET_FILE = 'C:\\Me\\Crypto\\Trading\\xtdotcomv1\\secret_key.txt';  
f = open(API_KEY_FILE, "r");  
API_KEY = f.read();
f.close();
f = open(API_SECRET_FILE, "r");  
API_SECRET = f.read();
f.close();
API_PASSPHRASE = '' 


gp = GetPositions(API_KEY, API_SECRET, API_PASSPHRASE)
gp.processJson()

go = GetOrders(API_KEY, API_SECRET, API_PASSPHRASE)
go.processJson()

cro = CreateOrder(API_KEY, API_SECRET, API_PASSPHRASE)
cro.processJson(product_id='', type='limit', side='buy', post_only=True, price=, size=)  

cao = CancelOrder(API_KEY, API_SECRET, API_PASSPHRASE)
cao.processJson('<tx_id>')
