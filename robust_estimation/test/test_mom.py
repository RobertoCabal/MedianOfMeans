from robust_estimation.MoM import MoM
import numpy as np
from scipy.stats import t

x = t.rvs(df=2, size=500)

def test_MoM():
    assert type(MoM(x,10))==np.float64
    assert type(MoM(x,15))==str