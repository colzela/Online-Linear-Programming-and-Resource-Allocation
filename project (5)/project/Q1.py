import numpy as np
from scipy.optimize import minimize
def oneTimeLearning(n = 10000, k = 50):
    e = 1e-10
    fun = lambda x:(x[0] - 0.667) / (x[0] + x[1] + x[2] - 2) # 目标函数
    cons = ({'type':'eq','fun':lambda x:x[0] * x[1] * x[2] - 1}, #约束条件：xyz=1
            {'type':'ineq','fun':lambda x:x[0]+x},             #x,y,z都分别大于0
            {'type':'ineq','fun':lambda x:x[1] - e},
            {'type':'ineq','fun':lambda x:x[2] - e})

    x0 = np.array((1.0,1.0,1.0)) #设置xyz的初始值
    res = minimize(fun,x0,method='SLSQP',constraints=cons)
