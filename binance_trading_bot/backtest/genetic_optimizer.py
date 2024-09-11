from deap import base, creator, tools, algorithms

def evaluate_strategy(individual):
    """Оценка стратегии с использованием бэктестинга."""
    rsi_period, stoch_period = individual
    final_balance = run_backtest_with_params(rsi_period, stoch_period)
    return final_balance,

def genetic_optimization():
    """Генетический алгоритм для оптимизации параметров."""
    creator.create("FitnessMax", base.Fitness, weights=(1.0,))
    creator.create("Individual", list, fitness=creator.FitnessMax)

    toolbox = base.Toolbox()
    toolbox.register("attr_int", random.randint, 10, 20)  # Пример параметров
    toolbox.register("individual", tools.initRepeat, creator.Individual, toolbox.attr_int, n=2)
    toolbox.register("population", tools.initRepeat, list, toolbox.individual)

    toolbox.register("evaluate", evaluate_strategy)
    toolbox.register("mate", tools.cxTwoPoint)
    toolbox.register("mutate", tools.mutFlipBit, indpb=0.05)
    toolbox.register("select", tools.selTournament, tournsize=3)
    toolbox.register("map", map)

    pop = toolbox.population(n=50)
    algorithms.eaSimple(pop, toolbox, cxpb=0.5, mutpb=0.2, ngen=40, verbose=True)
