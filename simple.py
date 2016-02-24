import numpy as np
import matplotlib.pyplot as plt
from scipy import optimize

def time(Y):
    v0 = 30
    X = 300
    g = 9.8
    return (-v0*np.hypot(X,Y) + np.sqrt(v0*v0*(X*X+Y*Y)+g*Y*(X*X+Y*Y)))/(g*Y)

def main():
    x = np.linspace(0,1000,500000)
    sol = optimize.minimize(time,0.1)
    plt.plot(x/2,time(x),'-',sol.x/2,sol.fun,'o')
    plt.savefig("aaa.png")
    print(sol)

if __name__ == "__main__":
    main()
