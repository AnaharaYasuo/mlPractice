import numpy as np
import matplotlib.pyplot as plt


def reg1dim(x, y):
    a = np.dot(x, y) / (x ** 2).sum()
    return a

if __name__ == "__main__":
    x = np.array([1,2,4,6,7])
    y = np.array([1,3,3,5,4])
    a=reg1dim(x, y)
    
    plt.scatter(x, y,color="k")
    plt.plot([0,x.max()],[0,a*x.max()],color="r")
    plt.show()