import numpy as np


def softplus(x):
    return np.log(1 + np.exp(x))


def softplus2(x):
    return max(0, x) + np.log(1 + np.exp(-abs(x)))


if __name__ == "__main__":
    print(softplus2(1000))
