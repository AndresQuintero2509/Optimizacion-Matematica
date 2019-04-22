
#Recuperado
#https://share.cocalc.com/share/4bfb9fc2-c03f-4f81-b8f3-c809763900a5/LM.ipynb?viewer=share

import numpy as np
from scipy.optimize import root

def func2(x):
    f = [x[0] * np.cos(x[1]) - 4,
         x[1]*x[0] - x[1] - 5]
    df = np.array([[np.cos(x[1]), -x[0] * np.sin(x[1])],
                   [x[1], x[0] - 1]])
    return f, df
sol = root(func2, [1, 1], jac=True, method='lm')
sol.x
