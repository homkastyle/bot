from strategies.adaptive_strategy import adaptive_strategy
from strategies.real_time_strategy import run_real_time_strategy
from portfolio.portfolio_manager import rebalance_portfolio
from utils.telegram_notifier import send_telegram_message
from utils.restart_manager import restart_bot_on_failure

def run_trading_bot():
    """Запуск всех основных модулей торгового бота."""
    try:
        # Запуск стратегии в реальном времени
        run_real_time_strategy()

        # Адаптивная стратегия
        adaptive_strategy(market_data, risk_level=1)

        # Ребалансировка портфеля
        rebalance_portfolio(assets=["BTC", "ETH"], target_allocations={"BTC": 0.6, "ETH": 0.4})

        # Отправка уведомлений
        send_telegram_message("Торговый бот успешно запущен и работает.")

    except Exception as e:
        print(f"Ошибка в торговом боте: {e}")
        restart_bot_on_failure()

if __name__ == "__main__":
    run_trading_bot()
