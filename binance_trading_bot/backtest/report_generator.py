import json

def calculate_metrics(trades):
    """Расчет ключевых метрик на основе сделок"""
    total_profit = 0
    total_loss = 0
    profitable_trades = 0
    losing_trades = 0
    max_profit = -float('inf')
    max_loss = float('inf')
    total_trades = len(trades)
    
    if total_trades == 0:
        return None

    for trade in trades:
        profit = trade['profit']
        if profit > 0:
            total_profit += profit
            profitable_trades += 1
            if profit > max_profit:
                max_profit = profit
        else:
            total_loss += profit
            losing_trades += 1
            if profit < max_loss:
                max_loss = profit

    avg_trade_size = (total_profit + total_loss) / total_trades
    win_rate = (profitable_trades / total_trades) * 100 if total_trades > 0 else 0

    metrics = {
        "total_trades": total_trades,
        "profitable_trades": profitable_trades,
        "losing_trades": losing_trades,
        "win_rate": win_rate,
        "average_trade_size": avg_trade_size,
        "max_profit": max_profit,
        "max_loss": max_loss,
    }

    return metrics

def save_metrics_to_json(metrics, file_path="trade_metrics.json"):
    """Сохранение метрик в JSON файл"""
    with open(file_path, 'w') as f:
        json.dump(metrics, f, indent=4)
    print(f"Метрики сохранены в файл: {file_path}")

def generate_report(trades, file_path="trade_metrics.json"):
    """Генерация и сохранение отчета по ключевым метрикам"""
    metrics = calculate_metrics(trades)
    if metrics:
        save_metrics_to_json(metrics, file_path)
    return metrics
