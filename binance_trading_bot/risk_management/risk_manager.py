from indicators.technical_indicators import calculate_volatility

def adjust_risk_by_volatility(market_data, risk_level=1):
    """Адаптивное управление рисками на основе волатильности."""
    volatility = calculate_volatility(market_data)
    stop_loss = risk_level * (0.02 + volatility)
    position_size = 100 / volatility  # Примерная формула управления риском
    return stop_loss, position_size
