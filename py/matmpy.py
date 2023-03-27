import pandas as pd
import numpy as np

def mat_mpy(mat_a: pd.DataFrame, mat_b: pd.DataFrame) -> pd.DataFrame:
    """Return the mastrix-multiplication of mat_a and mat_b."""
    return np.matmul(mat_a, mat_b)
