import pandas as pd
from catboost import CatBoostClassifier
from sklearn.metrics import f1_score
from sklearn.model_selection import train_test_split


class ScoreCatBoostClassifier:
    def f1_score(self, filename, target, features):
        df = pd.read_csv(filename)
        X_train, X_test, y_train, y_test = train_test_split(df[features], df[target])
        cb = CatBoostClassifier(verbose=False).fit(X_train, y_train)
        return f1_score(y_test, cb.predict(X_test))

