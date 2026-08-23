from matplotlib import pyplot as plt
import numpy as np
def f(x):
    return x**3 + x -1

a = 0
b = 1
tol = 1e-4

x = np.linspace(0, 1, 300)
y = f(x)
plt.plot(x, y, color='red')

fa = f(a)
fb = f(b)

roots = []

while (b-a)/2 > tol: 
    c = (a+b)/2
    roots.append(c)
    fc = f(c)

    if (fc > 0 and fa < 0) or (fc < 0 and fa > 0):
        b = c
        fb = fc
    else:
        a = c
        fa = fc

xc = (a+b)/2  
roots.append(xc)

print(xc)   

plt.plot(roots, np.linspace(1.5, 0.4, len(roots)), marker='o') 
plt.axvline(x=xc, linestyle='dashed', color='black')
plt.axhline(y=0, linestyle='dashed', color='black')
plt.xlabel('Iteration')

plt.ylabel('Root estimate (c)')   
plt.title('Convergence of Bisection Method')
plt.grid(True)
plt.show()

