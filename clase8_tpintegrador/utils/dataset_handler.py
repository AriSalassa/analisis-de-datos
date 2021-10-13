import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split


def split_dataset(X_input: pd.core.frame.DataFrame):
    # Complete me
    return


def clean_colums(X_in: pd.core.frame.DataFrame, max_nans_percentage: float = 15.0):
    nan_percentage = 100.0 * X_in.isna().sum() / X_in.shape[0]
    drop_columns = nan_percentage[nan_percentage > max_nans_percentage].to_frame()
    X_out = X_in.drop(list(drop_columns.index), axis=1).copy()
    print("Dropped columns:", drop_columns)
    return X_out
