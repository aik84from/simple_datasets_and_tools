import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_score


class ScoreRandomForestClassifier:
    def cross_val_score(self, filename, target, features):
        df = pd.read_csv(filename)
        model = RandomForestClassifier(n_estimators=2000, max_depth=150)
        return cross_val_score(model, df[features], df[target], cv=5, scoring='f1')

