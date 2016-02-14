from scipy import special, optimize
import numpy as np
import matplotlib.pyplot as plt

#gravitational acceleration (9.8m/s)
g = 9.8

def time(dx,dy,v0):
    return np.hypot(dx,dy) * (np.sqrt(v0*v0+2*g*dy) - v0) / (g*dy)

def new_verocity(dy,v0):
    return np.sqrt(v0*v0+2*g*dy)

def f(y):
    #length of one side (300m)
    L = 300
   
    #initial verocity (10m/s)
    v0 = 10
    v1 = new_verocity(np.absolute(y),v0)
    return time(L/2,np.absolute(y),v0) + time(L/2,np.absolute(y),v1)

y = np.linspace(start = 0, stop = 10, num = 101)
plt.plot(y, f(y))
plt.show()

