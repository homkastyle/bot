import time
from binance_connector import get_binance_client

def sync_time():
    client = get_binance_client()
    server_time = client.get_server_time()
    local_time = time.time() * 1000
    time_diff = server_time['serverTime'] - local_time
    return time_diff
