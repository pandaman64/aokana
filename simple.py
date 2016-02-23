import numpy as np
import matplotlib.pyplot as plt

def time(Y):
    v0 = 30
    X = 300
    g = 9.8
    return (-v0*np.hypot(X,Y) + np.sqrt(v0*v0*(X*X+Y*Y)+g*Y*(X*X+Y*Y)))/(g*Y)

def main():
    x = np.linspace(0,1000,500000)
    plt.plot(x/2,time(x))
    plt.savefig("aaa.png")

if __name__ == "__main__":
    main()
