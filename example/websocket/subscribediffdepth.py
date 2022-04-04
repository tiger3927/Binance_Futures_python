import logging
from binance_f import SubscriptionClient
from binance_f.constant.test import *
from binance_f.model import *
from binance_f.exception.binanceapiexception import BinanceApiException

from binance_f.base.printobject import *

logger = logging.getLogger("binance-futures")
logger.setLevel(level=logging.INFO)
handler = logging.StreamHandler()
handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
logger.addHandler(handler)

sub_client = SubscriptionClient(api_key=g_api_key, secret_key=g_secret_key)

count=0

def callback(data_type: 'SubscribeMessageType', event: 'any'):
    global  count
    count+=1
    if data_type == SubscribeMessageType.RESPONSE:
        print("Event ID: ", event)
    elif  data_type == SubscribeMessageType.PAYLOAD:
        print(event)
        #PrintMix.print_data(event.bids)
        e:diffdepthevent.DiffDepthEvent=event
        print(count,e.eventTime,e.firstUpdateId,e.finalUpdateId,e.lastUpdateIdInlastStream)
    else:
        print("Unknown Data:")
    print()


def error(e: 'BinanceApiException'):
    print(e.error_code + e.error_message)

sub_client.subscribe_diff_depth_event("btcusdt", callback, error, update_time=UpdateTime.FAST)  #UpdateTime.REALTIME
#sub_client.subscribe_diff_depth_event("btcusdt", callback, error, update_time=UpdateTime.FAST)
#sub_client.subscribe_diff_depth_event("btcusdt", callback, error, update_time=UpdateTime.NORMAL)
#sub_client.subscribe_diff_depth_event("btcusdt", callback, error)
