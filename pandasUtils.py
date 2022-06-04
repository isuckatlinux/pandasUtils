import pandas as pd
import numpy as np

def add_columns(df, col_names:list, columns:list, fill_value=None):
    """
    Add columns to a dataframe.
    These columns must be given as list or tuple
    """
    if len(col_names) != len(columns):
        raise Exception("Number of column names and columns must be equal")
    for col in columns:
        if type(col) not in (list, tuple):
            raise Exception("Columns must be a list of lists or tuples.")
    
    if fill_value == None:
        fill_value = np.nan

    for i, name in enumerate(col_names):
        df1 = pd.DataFrame({name:columns[i]})
        df = pd.concat([df, df1], axis=1)
        df.fillna(fill_value, inplace=True)
    return df