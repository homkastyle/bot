from utils.binance_connector import get_binance_client, safe_api_call
import pandas as pd
import logging

def fetch_market_data(pair, timeframe="15m"):
    client = get_binance_client()
    if not client:
        logging.error("Не удалось подключиться к Binance API.")
        return None
    
    try:
        klines = safe_api_call(client.get_klines, symbol=pair, interval=timeframe)
        if klines:
            df = pd.DataFrame(klines, columns=[
                'timestamp', 'open', 'high', 'low', 'close', 'volume', 
                'close_time', 'quote_asset_volume', 'number_of_trades',
                'taker_buy_base', 'taker_buy_quote', 'ignore'
            ])
            df['close'] = df['close'].astype(float)
            return df
        else:
            logging.error(f"Ошибка при получении данных рынка для пары {pair}.")
            return None
    except Exception as e:
        logging.error(f"Ошибка при обработке данных: {e}")
        return None
