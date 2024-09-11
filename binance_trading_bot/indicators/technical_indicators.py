import pandas as pd

def moving_average(data, window=14):
    """Расчет простой скользящей средней (SMA)"""
    return data['close'].rolling(window=window).mean()

def bollinger_bands(data, window=14, std_dev=2):
    """Расчет полос Боллинджера"""
    sma = moving_average(data, window)
    std = data['close'].rolling(window=window).std()
    upper_band = sma + (std_dev * std)
    lower_band = sma - (std_dev * std)
    return upper_band, lower_band

def calculate_atr(data, window=14):
    """Расчет Average True Range (ATR)"""
    data['high_low'] = data['high'] - data['low']
    data['high_close'] = abs(data['high'] - data['close'].shift())
    data['low_close'] = abs(data['low'] - data['close'].shift())

    tr = data[['high_low', 'high_close', 'low_close']].max(axis=1)
    atr = tr.rolling(window=window).mean()

    return atr
