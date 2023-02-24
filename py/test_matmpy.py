import pandas as pd
from pandas.testing import assert_frame_equal
import numpy as np
import matmpy

def test_matmpy():
    mat_a = pd.read_csv('/opt/data/mat_a.csv', index_col=None, header=None)
    mat_b = pd.read_csv('/opt/data/mat_b.csv', index_col=None, header=None)    
    expected = pd.read_csv('/opt/data/mat_c.csv', index_col=None, header=None)    

    actual = matmpy.mat_mpy(mat_a, mat_b)
    assert_frame_equal(expected, actual)

def test_matmpy_def():
    mat_d = pd.read_csv('/opt/data/mat_d.csv', index_col=None, header=None)
    mat_e = pd.read_csv('/opt/data/mat_e.csv', index_col=None, header=None)
    expected = pd.read_csv('/opt/data/mat_f.csv', index_col=None, header=None)    

    actual = matmpy.mat_mpy(np.asarray(mat_d), mat_e)
    assert_frame_equal(expected, actual)
