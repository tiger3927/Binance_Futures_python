from binance_f import RequestClient
from binance_f.constant.test import *
from binance_f.base.printobject import *
from binance_f.model.constant import *

request_client = RequestClient(api_key="", secret_key="")
#result = request_client.post_order(symbol="BTCUSDT", side=OrderSide.SELL, ordertype=OrderType.STOP_MARKET,
#                                   stopPrice=8000.1, closePosition=True, positionSide="LONG")
result=request_client.get_position_mode()


PrintBasic.print_obj(result)
