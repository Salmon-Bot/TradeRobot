import talib as ta
import numpy as np

p = np.array([1.0,2.0,3.0,4.0,5.0])
s = ta.MA(p, 5)
print(s)