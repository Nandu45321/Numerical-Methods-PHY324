from matplotlib import pyplot as plt
import numpy as np
def f(x):
    return x**3 + x - 1

def df(x):
    return 3*x**2 + 1

x0 = 1.0
tol = 1e-5

x = np.linspace(0, 1, 300)
y = f(x)
plt.plot(x, y, color='red')

roots = [x0]
 
while True: 
    x1 = x0 - f(x0)/df(x0)
    roots.append(x1)
    
    if abs(x1 - x0) < tol:
        break
        
    x0 = x1

xc = roots[-1]

print(xc)   

plt.plot(roots, np.linspace(1.5, 0.2, len(roots)), marker='o') 
plt.axvline(x=xc, linestyle='dashed', color='black')
plt.axhline(y=0, linestyle='dashed', color='black')
plt.xlabel('Iteration')
  
plt.ylabel('Root estimate (x)')   
plt.title("Convergence of Newton's Method") 
plt.grid(True)
plt.show()

