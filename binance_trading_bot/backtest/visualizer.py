from curses.ascii import alt


def plot_backtest_results(df, balance_history, metrics, title="Результаты бэктестинга", save_path=None):
    """Визуализация результатов с ключевыми метриками и графиками"""
    fig, (ax1, ax2, ax3) = alt.subplots(3, 1, figsize=(10, 10), sharex=True)

    # График цен
    ax1.plot(df['timestamp'], df['close'], label='Цена AAVE/USDT', color='blue')
    ax1.set_ylabel('Цена (USDT)', color='blue')
    ax1.set_title('Цена AAVE/USDT')

    # График изменения баланса
    ax2.plot(df['timestamp'], balance_history, label='Баланс', color='green')
    ax2.set_ylabel('Баланс (USDT)', color='green')
    ax2.set_title('Изменение баланса')

    # Расчет и отображение просадки
    drawdown, max_drawdown = calculate_drawdown(balance_history)
    ax3.plot(df['timestamp'], drawdown, label='Просадка', color='red')
    ax3.set_ylabel('Просадка (%)', color='red')
    ax3.set_title(f'Просадка (максимальная: {max_drawdown*100:.2f}%)')

    # Вывод ключевых метрик на график
    fig.suptitle(f"Ключевые метрики:\n"
                 f"Средний размер сделки: {metrics['average_trade_size']:.2f} USDT\n"
                 f"Макс. прибыль: {metrics['max_profit']:.2f} USDT\n"
                 f"Макс. убыток: {metrics['max_loss']:.2f} USDT\n"
                 f"Процент прибыльных сделок: {metrics['win_rate']:.2f}%")

    fig.tight_layout()

    # Сохранение графика в файл
    if save_path:
        alt.savefig(save_path)
        print(f"График сохранен в файл: {save_path}")
    
    alt.show()

def visualize_strategy_performance(df, balance_history, metrics, save_path=None):
    """Визуализация и сохранение изменения баланса, просадки и прибыли с метриками"""
    plot_backtest_results(df, balance_history, metrics, title="Выполнение стратегии", save_path=save_path)
    
    cumulative_returns = calculate_cumulative_returns(balance_history, initial_balance=100)
    
    fig, ax = alt.subplots(figsize=(10, 4))
    ax.plot(df['timestamp'], cumulative_returns, label='Кумулятивная прибыль', color='purple')
    ax.set_ylabel('Кумулятивная прибыль (%)')
    ax.set_title('Кумулятивная прибыль от начального баланса')
    
    if save_path:
        alt.savefig(save_path.replace('.png', '_returns.png'))
        print(f"График кумулятивной прибыли сохранен в файл: {save_path.replace('.png', '_returns.png')}")

    alt.show()
