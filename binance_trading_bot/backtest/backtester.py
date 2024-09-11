import logging
from strategies.multi_strategy import multi_strategy
from utils.logger import setup_logger
import pandas as pd

def run_backtest_with_multiple_strategies(file_path="data/market_data.csv", pair="AAVEUSDT", timeframe="15m"):
    df = pd.read_csv(file_path)  # Загружаем данные из CSV
    setup_logger()

    # Определяем стратегии для тестирования
    strategies = [
        {'type': 'stoch_rsi', 'rsi_period': 14, 'stoch_period': 14},
        {'type': 'ma', 'window': 50},
        {'type': 'bollinger_bands', 'window': 20}
    ]

    final_balance = multi_strategy(df, strategies)
    logging.info(f"Итоговый баланс после бэктеста с несколькими стратегиями: {final_balance}")
    return final_balance
