import numpy as np 
x = np.array([[0, 3], [4, 3], [6, 8]])
print(np.linalg.norm(x, axis = 1, keepdims = True))
print(np.linalg.norm(x))
print(np.linalg.norm(x, axis = 0, keepdims = True))
