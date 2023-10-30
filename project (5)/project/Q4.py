import numpy as np
import cvxpy as cp
import random
import pandas as pd
import math
k = 100
n = 10000    # number of bidders
m = 10       # type of resources

A = pd.read_csv("A.csv")
pi = pd.read_csv("pi.csv")

A = np.array(A)
A1 = A[:m, :k]
pi = np.array(pi)
b = np.array([1000 for _ in range(m)])  
pi1 = pi[:k]
pi1 = pi1.T
print(pi1.shape)

def u(s,w):
    value = 0
    for i in range(m):
        value += w/m * cp.log(s[i])
    return value
x = cp.Variable(k)
s = cp.Variable(m)
obj = cp.Maximize(pi1@x + u(s,1))
cons = [A1@x + s <= k/n * b, x>=0, x<=1]
prob = cp.Problem(obj, cons)
# prob.solve(solver="ECOS")
prob.solve(solver="SCS")
print("optimal solution of primal problem")
print(x.value)
print("optimal dual solution is")
print(prob.constraints[0].dual_value)
print("optimal value")
print(prob.value)

# print(piNow)