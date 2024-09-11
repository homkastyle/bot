import numpy as np

def optimize_stoch_rsi(data):
    best_params = None
    best_profit = -np.inf

    for rsi_period in range(10, 20):  # Оптимизация длины RSI
        for stoch_period in range(10, 20):  # Оптимизация длины Stochastic
            stoch_k, stoch_d = calculate_stoch_rsi(data, rsi_period, stoch_period)
            profit = simulate_trading(data, stoch_k, stoch_d)
            if profit > best_profit:
                best_profit = profit
                best_params = (rsi_period, stoch_period)

    print(f"Лучшие параметры RSI: {best_params[0]}, Stochastic: {best_params[1]}")
    return best_params

def simulate_trading(data, stoch_k, stoch_d):
    # Простая симуляция для оценки прибыльности стратегии
    profit = 0
    position = None
    for i in range(1, len(data)):
        if stoch_k[i] < 20 and stoch_d[i] < 20:
            if position != "long":
                position = "long"
                entry_price = data['close'][i]
        elif stoch_k[i] > 80 and stoch_d[i] > 80:
            if position == "long":
                position = None
                profit += (data['close'][i] - entry_price)
    return profit
