import logging

# Настройка логирования
def setup_logger():
    logging.basicConfig(
        filename="logs/trade_logs.log",
        level=logging.INFO,
        format="%(asctime)s %(levelname)s: %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )
    logging.info("Торговый бот запущен.")

def log_trade(action, pair, amount, price):
    logging.info(f"{action} {pair} на сумму {amount} по цене {price}")
