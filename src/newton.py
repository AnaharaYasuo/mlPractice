import numpy as np
from numpy import linalg


class Newton:

    def __init__(self, f, df, eps=1e-10, max_iter=1000):
        self.f = f
        self.df = df
        self.eps = eps
        self.max_iter = max_iter

    def solve(self, x0):
        x = x0
        itr = 0
        self.path_ = x0.reshape(1, -1)
        while True:
            x_new = x - np.dot(linalg.inv(self.df(x)), self.f(x))
            self.path_ = np.r_[self.path_, x_new.reshape(1, -1)]
            if ((x - x_new) ** 2).sum() < self.eps * self.eps:
                break
            x = x_new
            itr += 1
            if itr == self.max_iter:
                break
