from binance import Client
from binance.stream import BinanceSocketManager
from config import API_KEY, API_SECRET

def get_binance_client():
    return Client(API_KEY, API_SECRET)

def start_websocket(pair, callback):
    """Запуск WebSocket для получения данных в реальном времени."""
    client = get_binance_client()
    bm = BinanceSocketManager(client)