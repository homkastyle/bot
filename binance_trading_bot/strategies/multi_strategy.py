import logging

from binance_trading_bot.indicators.technical_indicators import bollinger_bands


def multi_strategy(df, strategies):
    """Бэктестинг нескольких стратегий с записью истории баланса"""
    position = None
    balance = 100  # Начальный баланс
    investment = 2  # Начальный размер позиции
    balance_history = [balance]

    for i in range(1, len(df)):
        stop_loss, position_size = apply_risk_management(df.iloc[:i])

        # Применение всех стратегий
        for strategy in strategies:
            if strategy['type'] == 'stoch_rsi':
                stoch_k, stoch_d = calculate_stoch_rsi(df.iloc[:i], strategy['rsi_period'], strategy['stoch_period'])
                if stoch_k.iloc[-1] < 20 and stoch_d.iloc[-1] < 20 and position is None:
                    position = 'long'
                    entry_price = df['close'].iloc[i]
                    logging.info(f"Открытие длинной позиции по цене {entry_price} с размером {position_size}")
                elif stoch_k.iloc[-1] > 80 and stoch_d.iloc[-1] > 80 and position == 'long':
                    profit = (df['close'].iloc[i] - entry_price) * position_size
                    balance += profit
                    balance_history.append(balance)
                    logging.info(f"Закрытие позиции с прибылью {profit}. Баланс: {balance}")
                    position = None

            if strategy['type'] == 'ma':
                sma = moving_average(df.iloc[:i], strategy['window'])
                if df['close'].iloc[-1] > sma.iloc[-1] and position is None:
                    position = 'long'
                    entry_price = df['close'].iloc[i]
                    logging.info(f"Открытие позиции по цене {entry_price}")
                elif df['close'].iloc[-1] < sma.iloc[-1] and position == 'long':
                    profit = (df['close'].iloc[i] - entry_price) * position_size
                    balance += profit
                    balance_history.append(balance)
                    logging.info(f"Закрытие позиции с прибылью {profit}. Баланс: {balance}")
                    position = None

            if strategy['type'] == 'bollinger_bands':
                upper_band, lower_band = bollinger_bands(df.iloc[:i], strategy['window'])
                if df['close'].iloc[-1] < lower_band.iloc[-1] and position is None:
                    position = 'long'
                    entry_price = df['close'].iloc[i]
                    logging.info(f"Открытие позиции по цене {entry_price}")
                elif df['close'].iloc[-1] > upper_band.iloc[-1] and position == 'long':
                    profit = (df['close'].iloc[i] - entry_price) * position_size
                    balance += profit
                    balance_history.append(balance)
                    logging.info(f"Закрытие позиции с прибылью {profit}. Баланс: {balance}")
                    position = None

        # Применение стоп-лосса
        if position == 'long' and df['close'].iloc[i] <= entry_price * (1 - stop_loss):
            loss = (entry_price - df['close'].iloc[i]) * position_size
            balance -= loss
            balance_history.append(balance)
            logging.info(f"Срабатывание стоп-лосса. Убыток: {loss}. Баланс: {balance}")
            position = None

    return balance, balance_history
