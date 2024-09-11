from utils.binance_connector import start_websocket

def process_message(msg):
    """Обработка полученных данных через WebSocket."""
    print(f"Получены данные: {msg['s']} цена: {msg['c']}")

def run_real_time_strategy(pair="AAVEUSDT"):
    """Запуск стратегии на основе данных в реальном времени."""
    conn_key = start_websocket(pair, process_message)
    print(f"WebSocket запущен для {pair}, ключ подключения: {conn_key}")
