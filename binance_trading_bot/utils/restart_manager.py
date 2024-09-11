import os

from binance_trading_bot.bot import run_trading_bot

def restart_bot_on_failure():
    """Перезапуск бота при сбое."""
    try:
        run_trading_bot()
    except Exception as e:
        print(f"Произошла ошибка: {e}. Перезапуск бота.")
        os.system('python bot.py')
