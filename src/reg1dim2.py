import numpy as np
import matplotlib.pyplot as plt


def reg1dim2(x, y):
    n = len(x)
    a = (np.dot(x, y) - x.sum() * y.sum() / n) / ((x ** 2).sum() - x.sum() ** 2 / n)
    b = (y.sum() - a * x.sum()) / n
    return a, b


if __name__ == "__main__":
    x = np.array([1, 2, 4, 6, 7])
    y = np.array([1, 3, 3, 5, 4])
    a, b = reg1dim2(x, y)
    
    plt.scatter(x, y, color="k")
    plt.plot([0, x.max()], [b, a * x.max() + b], color="r")
    plt.show()
