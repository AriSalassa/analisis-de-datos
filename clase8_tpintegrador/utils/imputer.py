import pandas as pd
import numpy as np
from sklearn.experimental import enable_iterative_imputer
from sklearn.impute import IterativeImputer


class Imputer:
    def __init__(self, name):
        super().__init__()
        self.name = name
        self.iter_imputer = None
        self.X_in_mode = None
        self.X_in_mean = None
        self.X_in_median = None

    def fill_missing_category_with_mode(self, X_in: pd.core.frame.DataFrame):
        if self.X_in_mode is None:
            self.X_in_mode = X_in.mode().iloc[0]

        X_out = X_in.fillna(self.X_in_mode)
        return X_out

    def fill_missgin_missing_category_with_new_cat(self, X_in: pd.core.frame.DataFrame):
        X_out = X_in.fillna(value="MISSING")
        return X_out

    def fill_missing_numerical_with_mean(self, X_in: pd.core.frame.DataFrame):
        if self.X_in_mean is None:
            self.X_in_mean = X_in.mean(axis=0)

        X_out = X_in.fillna(self.X_in_mean)
        return X_out

    def fill_missing_numerical_with_median(self, X_in: pd.core.frame.DataFrame):
        if self.X_in_median is None:
            self.X_in_median = X_in.median(axis=0)

        X_out = X_in.fillna(self.X_in_median)
        return X_out

    def fill_missing_numerical_mice(
        self,
        X_in: pd.core.frame.DataFrame,
        max_iter: int = 10,
        n_nearest_features: int = None,
    ):
        if self.iter_imputer == None:
            self.iter_imputer = IterativeImputer(
                n_nearest_features=n_nearest_features, max_iter=max_iter
            )
            self.iter_imputer.fit(X_in)

        cols = X_in.columns
        iter_imputed = self.iter_imputer.transform(X_in)
        X_out = pd.DataFrame(iter_imputed, columns=cols)

        return X_out
