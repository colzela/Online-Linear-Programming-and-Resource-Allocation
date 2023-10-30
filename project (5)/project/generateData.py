import numpy as np
import math
import random
import pandas as pd

n = 10000    # number of bidders
m = 10       # type of resources
b = np.array([1000 for _ in range(m)])      # inventory: m*1
p = np.array([float(random.gauss(0.5,0.1)) for _ in range(m)])      # ground truth price vector: m*1
A = np.random.randint(0, high = 2, size = (m, n))

pi = (p.T).dot(A)
for i in range(n):
    pi[i] += random.gauss(0, 0.2)

p = pd.DataFrame(p)
p.to_csv('p_3.csv',index=False)

pi = pd.DataFrame(pi)
pi.to_csv('pi_3.csv',index=False)

A = pd.DataFrame(A)
A.to_csv('A_3.csv',index=False)
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          