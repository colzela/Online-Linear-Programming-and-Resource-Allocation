import numpy as np
import math
import random
import pandas as pd

n = 10000    # number of bidders
m = 10       # type of resources
np.random.seed(0)
b = np.array([1000.0 for _ in range(m)])      # inventory: m*1
p = np.array(list(range(1,m+1)))      # ground truth price vector: m*1
A = np.random.randint(0, high = 2, size = (m, n))
A = A.astype('float64')
pi = np.matmul(p, A) + np.random.randn(n)*np.sqrt(0.2)


pi_ = pd.DataFrame(pi)
pi_.to_csv('pi_3.csv',index=False)

A_ = pd.DataFrame(A)
A_.to_csv('A_3.csv',index=False)

## Dependent gerenate
A_dependent = []
Pi_dependent = []
a = A[:,0]
pi_d = pi[0]
A_dependent.append(a.copy())
Pi_dependent.append(pi_d)
for i in range(n-1):
    a += np.round(np.random.randn(m)+2)
    pi_d += np.random.randn()+2.0
    A_dependent.append(a.copy())
    Pi_dependent.append(pi_d)

A_dependent = np.array(A_dependent)
A_dependent = A_dependent.T

Pi_dependent = np.array(Pi_dependent)
Pi_dependent = Pi_dependent.reshape(n,)

Pi_dependent_ = pd.DataFrame(Pi_dependent)
Pi_dependent_.to_csv('pi_dependent.csv',index=False)

A_dependent_ = pd.DataFrame(A_dependent)
A_dependent_.to_csv('A_dependent.csv',index=False)