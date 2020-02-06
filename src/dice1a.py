import numpy as np


def throw_dice(n):
    return np.random.randint(1, 7, size=n).sum()


if __name__ == "__main__":
    print (throw_dice(5))
    print (throw_dice(10))
