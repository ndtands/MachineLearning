''' Gradient Descent with singer parameter
    Function: f(x)= x^2 + 5*sin(x)
    => f'(x) = 2x+ 5*cos(x)
    x_t+1 = x_t-n*f'(x_t)
    n: Learing rate
'''

# To support both python 2 and python 3
from __future__ import division, print_function, unicode_literals
import math
import numpy as np 
import matplotlib.pyplot as plt

def grad(x):
    return 2*x+ 5*np.cos(x)


def cost(x):
    return x**2 + 5*np.sin(x)
#function using để mô tả quá trình tiến đến vị trí mà đạo hầm tại đó bằng 0
def myGD1(eta, x0):
    x = [x0]
    for it in range(100):
        x_new = x[-1] - eta*grad(x[-1]) # x_t+1 = x_t - n*f(x_t)'
        print("\n %f"%x_new)
        if abs(grad(x_new)) < 1e-3: #err <10^-3
            break
        x.append(x_new)
    return (x, it)


#innit with x0 = -5
(x1, it1) = myGD1(.1, -5)
#innit with x0 = 5
(x2, it2) = myGD1(.1, 5)
print('Solution x1 = %f, cost = %f, obtained after %d iterations'%(x1[-1], cost(x1[-1]), it1))
print('Solution x2 = %f, cost = %f, obtained after %d iterations'%(x2[-1], cost(x2[-1]), it2))