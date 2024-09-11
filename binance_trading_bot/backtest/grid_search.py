from backtest.report_generator import generate_report

def grid_search_optimization(df, param_grid, trades):
    """Параллельная оптимизация параметров с отчетом"""
    best_balance = -float('inf')
    best_params = None
    results_list = []

    param_combinations = list(itertools.product(*param_grid.values()))
    
    pool = mp.Pool(mp.cpu_count())
    results = pool.starmap(test_params, [(params, df) for params in param_combinations])
    pool.close()
    pool.join()

    for params, final_balance in results:
        print(f"Тестируемая комбинация: {params}, Баланс: {final_balance}")
        results_list.append({'params': params, 'balance': final_balance})

        if final_balance > best_balance:
            best_balance = final_balance
            best_params = params

    # Генерация отчета после оптимизации
    metrics = generate_report(trades)
    print(f"Лучшие параметры: {best_params} с балансом {best_balance}")
    return best_params, best_balance, results_list, metrics
