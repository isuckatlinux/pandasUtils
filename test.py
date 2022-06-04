import pandas as pd
import pandasUtils as pu

df = pd.DataFrame({"A": [1, 2, 3], "B": [4, 5, 6]})

lista = [1, 2, 3, 4, 5, 6]
tupla = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

df = pu.add_columns(df, col_names=["C", "D"], columns=[lista, tupla])

print(df)