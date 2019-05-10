import numpy as np

import matplotlib.pyplot as pt

def f(x):

    return 10 + x * np.log(x)

g=np.frompyfunc(f,1,1)

'''

把函数赋予ufunc属性，并记为g，接收一个参数，并返回一个参数。

'''

a=np.arange(0.1,100,0.00001)

d=g(a)

d_max=np.max(d)

d_min=np.min(d)

pt.figure(figsize=(5*2,2*3.65))

pt.xlim((0,100))

pt.ylim((0,10000))

pt.plot(a,d,'-',c='g',lw=2)

pt.show()
