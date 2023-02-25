import pandas as pd

def mat_mpy(mat_a: pd.DataFrame, mat_b: pd.DataFrame) -> pd.DataFrame:
    result = mat_a.dot(mat_b) # dot computes the matrix multiplication between the DataFrame and values of another series, DataFrame or a NumPy array.
    return result 

