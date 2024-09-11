from sklearn.ensemble import RandomForestClassifier

def train_model(X, y):
    """Обучение модели для прогнозирования направления рынка."""
    model = RandomForestClassifier(n_estimators=100)
    model.fit(X, y)
    return model

def predict_trend(model, X):
    """Прогнозирование на основе обученной модели."""
    return model.predict(X)
