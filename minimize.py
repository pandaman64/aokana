from scipy import special, optimize
import numpy as np
import matplotlib.pyplot as plt

#gravitational acceleration (9.8m/s)
g = 9.8

def time(dx,dy,v0):
    if(dy == 0):
        return dx/v0
    #return np.hypot(dx,dy) * (np.sqrt(v0*v0+2*g*dy) - v0) / (g*dy)
    ds = np.hypot(dx,dy)
    return (-v0*ds + np.sqrt((v0**2)*(ds**2)+g*dy*(ds**2)))/(g*dy)

def verocity(dy,v0):
    return np.sqrt(v0*v0+2*g*dy)

def f(ys):
    #number of intervals
    count = ys.size + 1
    #length of one side (300m)
    L = 300.0
    #length of one interval
    l = L / count
   
    #initial verocity (10m/s)
    v0 = 10
    t = 0
    y0 = 0
    for y in ys:
        dy = np.absolute(y0 - y)
        t += time(l,dy,v0)
        v0 = verocity(dy,v0)
        y0 = y

    #last interval
    t += time(l,np.absolute(y0),v0)
    return t

ys = [-1.0] + np.random.random_sample(100)
#sol = optimize.minimize(f,ys)
sol = optimize.basinhopping(f,ys,niter = 100)
print(sol)
print(sol.fun)
xs = np.linspace(0, 300.0 ,ys.size + 2)
plt.plot(xs,np.concatenate(([0],sol.x,[0])),'-')
plt.axhline(y=0,color='g')
plt.show()
