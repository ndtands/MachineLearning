''' FIND MIN OF FUNCTION :  f(x,y)=(x^2+y−7)^2+(x−y+1)^2 '''
#import library
from __future__ import division, print_function, unicode_literals
import matplotlib
import numpy as np
import matplotlib.cm as cm
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt

matplotlib.rcParams['xtick.direction'] = 'out'
matplotlib.rcParams['ytick.direction'] = 'out'

#function 
def cost(w):
    x = w[0]
    y = w[1]
    return (x**2 + y - 7)**2 + (x - y + 1)**2 
	# return x**2 + y**2

def grad(w):
	x = w[0]
	y = w[1]
	g = np.zeros_like(w)
	g[0] = 2*(x**2 + y - 7)*2*x + 2*(x - y + 1) #f(x,y)'x
	g[1] = 2*(x**2 + y - 7)     + 2*(y - x - 1) #f(x,y)'y
	return g

def numerical_grad(w, cost):
	eps = 1e-6
	g = np.zeros_like(w)
	for i in range(len(w)):
		w_p = w.copy()
		w_n = w.copy()
		w_p[i] += eps 
		w_n[i] -= eps
		g[i] = (cost(w_p) - cost(w_n))/(2*eps)
	return g 

def check_grad(w, cost, grad):
        w = np.random.rand(w.shape[0], w.shape[1])
        grad1 = grad(w)  #return W1x2
        grad2 = numerical_grad(w, cost) #W1x2
        return True if np.linalg.norm(grad1 - grad2) < 1e-4 else False #Caculator |A| < 10^-4

w = np.random.randn(2, 1) # random x and y (w0 and w1)
# w_init = np.random.randn(2, 1)

print( 'Checking gradient...', check_grad(w, cost, grad))

def myGD(w_init, grad, eta):
    w = [w_init]
    for it in range(200):
        w_new = w[-1] - eta*grad(w[-1])
		# print(w_new)
        #print( np.linalg.norm(grad(w_new)))
        if np.linalg.norm(grad(w_new))/len(w_new) < 1e-3:
            break 
        w.append(w_new)
		# print('iter %d: ' % it, w[-1].T)
    return (w, it) 

w_init = np.array([[-3], [-2.5]])
w_init = np.random.randn(2, 1)
(w1, it1) = myGD(w_init, grad, 0.05)
print(w1[-1])
# (w2, it2) = myGD(w_init, grad, 1)
# (w3, it3) = myGD(w_init, grad, 2)

# print(it1, it2, it3)
# print(w1, it1)
"""
delta = 0.025
x = np.arange(-6.0, 5.0, delta)
y = np.arange(-20.0, 15.0, delta)
X, Y = np.meshgrid(x, y)
Z = (X**2 + Y - 7)**2 + (X-Y + 1)**2
"""